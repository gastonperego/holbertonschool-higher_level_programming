-- lists all shows contained in the database hbtn_0d_tvshows
-- lists all shows contained in the database hbtn_0d_tvshows
SELECT title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.id LIKE '%' OR NULL ORDER BY title, genre_id;
