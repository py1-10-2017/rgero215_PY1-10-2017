SELECT users.first_name, users.last_name, friendships.friend_first_name, friendships.friends_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.friend_id = user2.id
ORDER BY user.last_name;