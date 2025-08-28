// client/GUI/static/app.js

// ===== CONFIG =====
const API_BASE = ""; // vuoto → fetch verso lo stesso host/porta del client Flask
const TOKEN_KEY = "authToken"; // chiave nel localStorage

// ===== AUTENTICAZIONE =====
function saveToken(token) {
    localStorage.setItem(TOKEN_KEY, token);
}

function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

function logout() {
    localStorage.removeItem(TOKEN_KEY);
    window.location.href = "/login";
}

// ===== FETCH GENERICO =====
async function apiFetch(endpoint, options = {}) {
    const token = getToken();
    const headers = options.headers || {};

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }
    headers["Content-Type"] = "application/json";

    const response = await fetch(API_BASE + endpoint, {
        ...options,
        headers
    });

    if (!response.ok) {
        console.error(`Errore API: ${response.status}`);
        throw new Error(`Errore API: ${response.status}`);
    }
    return await response.json();
}

// ===== LOGIN =====
async function handleLogin(event) {
    event.preventDefault();

    const username = document.querySelector('input[name="username"]').value;
    const password = document.querySelector('input[name="password"]').value;

    try {
        const result = await apiFetch("/auth/login", {
            method: "POST",
            body: JSON.stringify({ username, password })
        });

        if (result.status === "ok") {
            saveToken(result.token || "dummyToken");
            window.location.href = "/home";
        } else if (result.status === "blacklisted") {
            alert("Sei nella blacklist!");
        } else if (result.status === "not_found") {
            alert("Account inesistente. Registrati.");
        } else {
            alert(result.message || "Errore sconosciuto");
        }
    } catch (err) {
        console.error("Errore login:", err);
        alert("Impossibile effettuare il login. Controlla la connessione.");
    }
}

// ===== CARICAMENTO DATI UTENTE =====
async function loadUserData() {
    try {
        const user = await apiFetch("/user/me");
        document.querySelector("#username").innerText = user.username;
        document.querySelector("#email").innerText = user.email;
    } catch (err) {
        console.error("Impossibile caricare i dati utente:", err);
    }
}

// ===== INIZIALIZZAZIONE =====
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#loginForm");
    if (loginForm) {
        loginForm.addEventListener("submit", handleLogin);
    }

    if (document.body.dataset.page === "profile") {
        loadUserData();
    }
});
