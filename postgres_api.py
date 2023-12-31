import psycopg
import json
from dotenv import load_dotenv

load_dotenv()


class PostgresApi:

    def __init__(self, database_url="postgresql://postgres:example@localhost:5432/michaeledoror"):
        self.database_url = database_url

    def create_table(self):
        conn = psycopg.connect(self.database_url)

        cur = conn.cursor()

        cur.execute("""
        CREATE TYPE player_position AS ENUM ('QB', 'RB', 'WR', 'TE', 'K', 'D/ST');
        CREATE TYPE slot_position AS ENUM ('QB', 'RB', 'WR', 'TE', 'K', 'D/ST', 'BE', 'IR', 'OP', 'RB/WR/TE');

              CREATE TABLE fantasy_football_data (
                data_id serial primary key,
                points integer,
                team_id integer,
                stats_json jsonb,
                s_position slot_position,
                p_position player_position
            );

            ALTER TABLE fantasy_football_data 
            ADD CONSTRAINT fk_team
            FOREIGN KEY (team_id) 
            REFERENCES fantasy_football_teams(team_id);
        """)

        print("Table created successfully!")

        conn.commit()

        cur.close()
        conn.close()

    def delete_table(self):
        conn = psycopg.connect(self.database_url)

        cur = conn.cursor()

        cur.execute("""
            DROP TABLE IF EXISTS fantasy_football_data;
            DROP TYPE  IF EXISTS player_position;
            DROP TYPE  IF EXISTS slot_position;
         """)

        print("Tables deleted!")

        conn.commit()

        cur.close()
        conn.close()

    def insert_fantasy_football_data(self, payload):
        conn = psycopg.connect(self.database_url)

        cur = conn.cursor()

        cur.executemany("""
        INSERT INTO fantasy_football_data (points, team_id, stats_json, s_position, p_position)
        VALUES (%s, %s, %s::jsonb, %s, %s)
        """,
                        [(points, team_id, json.dumps(stats_json), s_position, p_position) for
                         points, team_id, stats_json, s_position, p_position in payload],
                        )

        print("Tables inserted!")

        conn.commit()

        cur.close()
        conn.close()
