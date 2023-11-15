-- script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows 
    ON tv_shows.id = tv_show_genres.show_id
    ORDER tv_shows.title, tv_show_genres.genre_id ASC;
