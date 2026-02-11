from flask import Blueprint, request, jsonify, render_template_string, session, redirect, url_for
import os
from markupsafe import Markup
from server.objects.user import User
from server.db.db_crud import verify_password
import urllib.request

bp = Blueprint('admin_ui', __name__, url_prefix='/admin')

def _load_template(name):
    tpl_path = os.path.join(os.path.dirname(__file__), 'templates', name)
    try:
        with open(tpl_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return None

def _get_state():
    # return shared sessions and mode_ref from api_server
    try:
        import server.logic.api_server as api_server
        return api_server.sessions, api_server.mode_ref
    except Exception:
        return {}, ["auto"]


@bp.route('/', methods=['GET'])
def index():
    # require admin login (ROOT or ADMIN)
    if not session.get('admin_user'):
        return redirect(url_for('admin_ui.login'))

    sessions, mode_ref = _get_state()
    pending = []
    try:
        import server.logic.admin_console as ac
        pending = ac.list_pending()
    except Exception:
        pending = []

    try:
        import server.services.email_service as es
        reset_tokens = es.reset_tokens
    except Exception:
        reset_tokens = {}

    try:
        import server.logic.api_server as api_server
        running = api_server.is_server_enabled()
    except Exception:
        running = False

    tpl = _load_template('admin_console.html')
    if tpl:
        return render_template_string(tpl, mode=mode_ref[0], pending=pending, tokens=list(sessions.keys()), reset_tokens=reset_tokens, running=running)
    # fallback: simple render
    return "Admin console template not found", 500



@bp.route('/approve', methods=['POST'])
def approve():
    action = request.form.get('action', 'accept')
    index = request.form.get('index')
    import server.logic.admin_console as ac
    approve_flag = (action == 'accept')
    try:
        if index is None:
            # default: process next
            cmd = 'k' if approve_flag else 'n'
            ac._process_approval(cmd)
            return jsonify({"result": "processed", "action": action})
        else:
            idx = int(index)
            ok = ac.process_approval_at(idx, approve_flag)
            if ok:
                return jsonify({"result": "processed", "index": idx, "action": action})
            return jsonify({"error": "index not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/login', methods=['GET', 'POST'])
def login():
        # simple admin login form + processing (GET renders styled form; POST authenticates)
        # Provide a minimal WTForms-like form object so template can render inputs and hidden_tag
        class _DummyField:
            def __init__(self, name, ftype='text', fid=None):
                self.name = name
                self.type = ftype
                self.id = fid or name
                self.errors = []
            def __call__(self, **kwargs):
                attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
                return Markup(f'<input type="{self.type}" name="{self.name}" id="{self.id}" {attrs} />')

        class _DummyForm:
            def __init__(self):
                self.username = _DummyField('username')
                self.password = _DummyField('password', ftype='password', fid='login_password')
            def hidden_tag(self):
                return Markup('')

        form = _DummyForm()

        if request.method == 'GET':
            tpl = _load_template('login_admin.html')
            if tpl:
                return render_template_string(tpl, form=form)
            return "Login template not found", 500

        # POST: authenticate
        username = (request.form.get('username') or '').strip()
        password = request.form.get('password') or ''
        if not username or not password:
            tpl = _load_template('login_admin.html')
            if tpl:
                return render_template_string(tpl, form=form, error='Missing credentials'), 400
            return render_template_string('<p>Missing credentials</p>'), 400

        user = User.get_user_by_username(username)
        if not user:
            tpl = _load_template('login_admin.html')
            if tpl:
                return render_template_string(tpl, form=form, error='User not found'), 401
            return render_template_string('<p>User not found</p>'), 401

        phash = user.get('password_hash') or user.get('password') or user.get('passwordHash')
        try:
            ok = verify_password(password, phash)
        except Exception:
            ok = False

        if not ok:
            tpl = _load_template('login_admin.html')
            if tpl:
                return render_template_string(tpl, form=form, error='Invalid credentials'), 401
            return render_template_string('<p>Invalid credentials</p>'), 401

        # Check user level: allow ROOT (0) and ADMIN (1)
        lvl = user.get('lvl')
        try:
            lvl = int(lvl) if lvl is not None else None
        except Exception:
            lvl = None

        if lvl not in (0, 1):
            tpl = _load_template('login_admin.html')
            if tpl:
                return render_template_string(tpl, form=form, error='User is not admin'), 403
            return render_template_string('<p>User is not admin</p>'), 403

        # success: set session and redirect to admin index
        session['admin_user'] = username
        return redirect(url_for('admin_ui.index'))


@bp.route('/logout_admin', methods=['POST', 'GET'])
def logout_admin():
    session.pop('admin_user', None)
    return redirect(url_for('admin_ui.login'))


@bp.route('/pending', methods=['GET'])
def pending_json():
    try:
        import server.logic.admin_console as ac
        items = ac.list_pending()
        # Return the metadata list as JSON
        return jsonify(items)
    except Exception as e:
            return jsonify({"error": str(e)}), 500


@bp.route('/switch', methods=['POST'])
def switch_mode():
    _, mode_ref = _get_state()
    mode_ref[0] = 'manual' if mode_ref[0] == 'auto' else 'auto'
    return jsonify({"mode": mode_ref[0]})


@bp.route('/start', methods=['POST'])
def start_server():
    try:
        import server.logic.api_server as api_server
        # enable logical service (so /api responds). keep WSGI server running.
        api_server.enable_server()
        return jsonify({"started": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/logout', methods=['POST'])
def logout():
    token = request.form.get('token')
    sessions, _ = _get_state()
    if token and token in sessions:
        sessions.pop(token, None)
        return jsonify({"result": "removed", "token": token})
    return jsonify({"error": "token not found"}), 404


@bp.route('/revoke_reset', methods=['POST'])
def revoke_reset():
    token = request.form.get('token')
    try:
        import server.services.email_service as es
        if token in es.reset_tokens:
            es.reset_tokens.pop(token, None)
            return jsonify({"result": "revoked", "token": token})
        return jsonify({"error": "token not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/stop', methods=['POST'])
def stop():
    try:
        import server.logic.api_server as api_server
        # logically pause the service so client API calls are rejected,
        # but keep admin UI available on the same WSGI server.
        api_server.disable_server()
        return jsonify({"stopped": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/_internal_shutdown', methods=['POST'])
def _internal_shutdown():
    # legacy endpoint — forward to controlled stop
    try:
        import server.logic.api_server as api_server
        api_server.stop_wsgi_server()
        return jsonify({"result": "shutting down"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
