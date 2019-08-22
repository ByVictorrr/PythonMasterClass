/*1.Select the titles of all the songs on the albums "Forbidden"
SELECT songs.title FROM songs INNER JOIN albums ON albums._id = songs.album WHERE albums.name="Forbidden";
*/

/*2. Reapeat previous query but this time display the songs in track order. You may want to include the track number in the output to verify that it worked ok
SELECT songs.title, songs.track  FROM songs INNER JOIN albums ON albums._id = songs.album WHERE albums.name="Forbidden" ORDER BY songs.track;
*/

/*3. Display all songs for the band "Deep Purple"
SELECT songs.title FROM songs 
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON artists._id = albums.artist
WHERE artists.name = "Deep Purple"
*/

/*4. Rename the band "Mehitabel" to "One Kitten". Note that this si an exception to the adivce to always fully qualify your column names. SET artists.name wont work, you just need to specify name.
UPDATE artists SET name="One Kitten" WHERE name="Mehitabel"

/*5. check that number 4 went good */ 
/*SELECT name FROM artists WHERE name="One Kitten"/*

/*6. Select the titles of all the songs by Aerosmith in alphabetic order. Include only the title in the output.
SELECT songs.title FROM songs 
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith"
ORDER BY songs.title;
*/
/*7. Replace the column that you used in the previous anser with count(title) to get just a count of the number of songs.
SELECT count(songs.title) FROM songs 
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith"
ORDER BY songs.title;
*/

/*8. Search the internet to find out how to get a list of the songs from step 6 without any duplicates

SELECT DISTINCT songs.title FROM songs 
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith"
ORDER BY songs.title;
*/


/*9. Search the internet again to find out how to get a count of the songs without duplicates. Hint: It uses the same keyword as step 8 but the syntax may not be obvious.

SELECT count(DISTINCT songs.title) FROM songs 
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith"
ORDER BY songs.title;

*/

/*10. Repeate the rpevious query to fin the number of artist (which , ob,oulsy should be one) and the number of albums.*/

SELECT count(DISTINCT artists.name), count(DISTINCT albums.name) FROM songs 
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith"



