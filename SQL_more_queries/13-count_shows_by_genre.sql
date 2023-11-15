--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres INNER JOIN tv_show_genres ON id = tv_show_genres.genre_id GROUP BY tv_show_genres.genre_id;