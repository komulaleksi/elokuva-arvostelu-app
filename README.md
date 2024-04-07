# elokuva-arvostelu-app

Rotten Tomatoes-tyylinen elokuvien arvostelusovellus, jossa käyttäjät voivat arvostella elokuvia antamalla niille arvosanan ja kirjoittamalla pienen arvostelun.

KÄYNNISTYSOHJEET: \
Kloonaa repositio omalle koneellesi ja luo juurikansioon tiedosto .env, jossa on seuraavat tiedot: \
DATABASE_URL=tietokannan-osoite \
SECRET_KEY=salainen-avain

Aktivoi virtuaaliympäristö ja asenna riippuvuudet seuraavilla tai vastaavilla komennoilla: \
$ python3 -m venv venv \
$ source venv/bin/activate \
$ pip install -r ./requirements.txt

Määritä vielä tietokannan skeema: \
psql < schema.sql

Sovelluksen voi käynnistää komennolla: \
flask run

Ohjelman käyttö:
Ensimmäisenä luotu käyttäjätunnus (user_id = 1) on ylläpitäjä, joka voi lisätä elokuvia tietokantaan elokuvat-sivulta (/movies). Ylläpitäjä ja muut käyttäjät voivat antaa elokuville pisteitä väliltä 1-5 ja kirjoittaa arvostelun, jotka näkyvät elokuvien sivulla.

-------------------------------------------------------------------------------------------------

Tämän hetkinen toiminnalisuus:
- Käyttäjä voi luoda käyttäjätunnuksen sekä kirjautua sisään ja ulos.
- Käyttäjä voi antaa elokuvalle pisteitä väliltä 1-5 sekä kirjoittaa elokuvalle arvostelun.
- Käyttäjä näkee jokaisesta elokuvasta käyttäjien antamien pisteiden keskiarvon.
- Ylläpitäjä voi lisätä elokuvia tietokantaan.
* Ylläpitäjä on ensimmäisenä luotu käyttäjä (user_id = 1)

Lopullisen sovelluksen ominaisuuksia:
- Käyttäjä voi luoda käyttäjätunnuksen sekä kirjautua sisään ja ulos.
- Käyttäjä voi hakea elokuvaa tietokannasta nimellä tai muilla tunnisteilla.
- Käyttäjä voi antaa elokuvalle pisteitä väliltä 1-5 sekä kirjoittaa elokuvalle lyhyen arvostelun.
- Käyttäjä näkee jokaisesta elokuvasta käyttäjien antamien pisteiden keskiarvon.
- Käyttäjä näkee omasta ja muiden profiilista käyttäjän antamat arvostelut.
- Ylläpitäjä voi lisätä ja poistaa elokuvia tietokantaan/-sta.
- Ylläpitäjä voi tarvittaessa poistaa käyttäjien arvosteluja.
