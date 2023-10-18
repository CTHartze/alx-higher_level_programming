-- Commands lists all genres and displays the number of shows linked to each from hbtn_0d_tvshows
-- Sets column names, does not display empty genre, in descending order
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
