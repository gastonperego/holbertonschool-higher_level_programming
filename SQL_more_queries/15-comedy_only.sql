-- lists all Comedy shows in the database hbtn_0d_tvshows
-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title FROM tv_shows INNER JOIN tv_show_genres ON id = tv_show_genres.show_id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE name = 'Comedy' ORDER BY title ASC; 