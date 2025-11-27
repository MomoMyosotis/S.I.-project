export class User {
  constructor({ id, username, followers, followed, bio, lvl }) {
    console.log("[DEBUG][User.constructor] Creating user:", { id, username, followers, followed, bio, lvl });

    this.id = id;
    this.username = username;
    this.followers = followers;
    this.followed = followed;
    this.bio = bio || "";
    this.lvl = lvl || "REGULAR";

    console.log("[DEBUG][User.constructor] User instance created:", this);
  }
}

export function userFromServer(data) {
  console.log("[DEBUG][userFromServer] Raw server data:", data);

  const user = new User({
    id: data.user_id,
    username: data.username,
    followers: data.followers_count,
    followed: data.following_count,
    bio: data.bio,
    lvl: data.lvl || "REGULAR",
  });

  console.log("[DEBUG][userFromServer] Transformed User object:", user);

  return user;
}
