-- ==============================================================
-- IPL Data Warehouse - Full Setup Script (Aligned with match_info & deliverables)
-- ==============================================================

USE kbnhzraf_ipl_stg;

-- ==============================================================
-- 1. Staging Tables
-- ==============================================================
DROP TABLE IF EXISTS kbnhzraf_ipl_stg.staging_matches;
CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_stg.staging_matches AS
SELECT
    match_number AS match_id,
    team1,
    team2,
    match_date AS date,
    toss_winner,
    toss_decision,
    result,
    eliminator,
    winner,
    player_of_match,
    venue,
    city
FROM kbnhzraf_ipl_db.match_info;

DROP TABLE IF EXISTS kbnhzraf_ipl_stg.staging_deliveries;
CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_stg.staging_deliveries AS
SELECT
    match_id,
    inning,
    batting_team,
    over_num AS over_number,
    ball_num AS ball,
    batter,
    bowler,
    non_striker,
    batsman_runs,
    extra_runs,
    total_runs,
    extras_type,
    is_wicket,
    player_dismissed,
    dismissal_kind,
    fielder
FROM kbnhzraf_ipl_db.deliverables;

-- ==============================================================
-- 3. Curated Tables
-- ==============================================================

USE kbnhzraf_ipl_dwh;


DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.curated_matches;
CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_dwh.curated_matches AS
SELECT DISTINCT *
FROM kbnhzraf_ipl_stg.staging_matches;

DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.curated_deliveries;
CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_dwh.curated_deliveries AS
SELECT * FROM kbnhzraf_ipl_stg.staging_deliveries;

-- ==============================================================
-- 4. Dimensions
-- ==============================================================


DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.fact_matches;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.fact_deliveries;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_match;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_player;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_team;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_date;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_venue;


-- Date Dimension
CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_dwh.dim_date (
    date_id INT PRIMARY KEY AUTO_INCREMENT,
    full_date DATE,
    day INT,
    month INT,
    month_name VARCHAR(20),
    quarter INT,
    year INT,
    weekday_name VARCHAR(10)
);

INSERT INTO kbnhzraf_ipl_dwh.dim_date (full_date, day, month, month_name, quarter, year, weekday_name)
SELECT DISTINCT
    date,
    DAY(date),
    MONTH(date),
    MONTHNAME(date),
    QUARTER(date),
    YEAR(date),
    DAYNAME(date)
FROM kbnhzraf_ipl_dwh.curated_matches;

-- Team Dimension

CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_dwh.dim_team (
    team_id INT PRIMARY KEY AUTO_INCREMENT,
    team_name VARCHAR(100)
);

INSERT INTO kbnhzraf_ipl_dwh.dim_team (team_name)
SELECT DISTINCT team1 FROM kbnhzraf_ipl_dwh.curated_matches
UNION
SELECT DISTINCT team2 FROM kbnhzraf_ipl_dwh.curated_matches
UNION
SELECT DISTINCT batting_team FROM kbnhzraf_ipl_dwh.curated_deliveries;

-- Player Dimension 
--SCD Type 2

CREATE TABLE kbnhzraf_ipl_dwh.dim_player (
    player_id INT PRIMARY KEY AUTO_INCREMENT,
    player_name VARCHAR(100)
);

INSERT INTO kbnhzraf_ipl_dwh.dim_player (player_name)
SELECT DISTINCT batter FROM kbnhzraf_ipl_dwh.curated_deliveries
UNION
SELECT DISTINCT bowler FROM kbnhzraf_ipl_dwh.curated_deliveries
UNION
SELECT DISTINCT fielder FROM kbnhzraf_ipl_dwh.curated_deliveries
UNION
SELECT DISTINCT player_of_match FROM kbnhzraf_ipl_dwh.curated_matches;

-- Venue Dimension

CREATE TABLE kbnhzraf_ipl_dwh.dim_venue (
    venue_id INT PRIMARY KEY AUTO_INCREMENT,
    venue_name VARCHAR(255),
    city VARCHAR(100),
	start_date DATE,
	end_date DATE,
	is_current TINYINT(1) DEFAULT 1
);

INSERT INTO kbnhzraf_ipl_dwh.dim_venue (venue_name,city,start_date,end_date,is_current)
SELECT DISTINCT venue,city,CURDATE(),NULL,1 FROM kbnhzraf_ipl_dwh.curated_matches;

-- Match Dimension
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_match;
CREATE TABLE kbnhzraf_ipl_dwh.dim_match (
    match_id INT PRIMARY KEY,
    toss_winner VARCHAR(100),
    toss_decision VARCHAR(10),
    winner VARCHAR(100),
    player_of_match VARCHAR(100),
    venue_id INT,
    date_id INT,
    FOREIGN KEY (venue_id) REFERENCES kbnhzraf_ipl_dwh.dim_venue(venue_id),
    FOREIGN KEY (date_id) REFERENCES kbnhzraf_ipl_dwh.dim_date(date_id)
);

INSERT INTO kbnhzraf_ipl_dwh.dim_match (match_id, toss_winner, toss_decision, winner, player_of_match, venue_id, date_id)
SELECT distinct 
    cm.match_id,
    cm.toss_winner,
    cm.toss_decision,
    cm.winner,
    cm.player_of_match,
    dv.venue_id,
    dd.date_id
FROM kbnhzraf_ipl_dwh.curated_matches cm
LEFT JOIN kbnhzraf_ipl_dwh.dim_venue dv ON cm.venue = dv.venue_name
LEFT JOIN kbnhzraf_ipl_dwh.dim_date dd ON cm.date = dd.full_date;

-- ==============================================================
-- 5. Fact Tables
-- ==============================================================

-- Fact Deliveries (Ball by Ball)

CREATE TABLE kbnhzraf_ipl_dwh.fact_deliveries (
    delivery_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT,
    batting_team_id INT,
    bowler_id INT,
    batter_id INT,
    fielder_id INT,
    over_number INT,
    ball INT,
    batsman_runs INT,
    extra_runs INT,
    total_runs INT,
    is_wicket TINYINT,
    FOREIGN KEY (match_id) REFERENCES kbnhzraf_ipl_dwh.dim_match(match_id),
    FOREIGN KEY (batting_team_id) REFERENCES kbnhzraf_ipl_dwh.dim_team(team_id),
    FOREIGN KEY (batter_id) REFERENCES kbnhzraf_ipl_dwh.dim_player(player_id),
    FOREIGN KEY (bowler_id) REFERENCES kbnhzraf_ipl_dwh.dim_player(player_id),
    FOREIGN KEY (fielder_id) REFERENCES kbnhzraf_ipl_dwh.dim_player(player_id)
);

INSERT INTO kbnhzraf_ipl_dwh.fact_deliveries (
    match_id, batting_team_id, bowler_id, batter_id, fielder_id,
    over_number, ball, batsman_runs, extra_runs, total_runs, is_wicket
)
SELECT
    cd.match_id,
    bt.team_id,
    bw.player_id,
    b.player_id,
    f.player_id,
    cd.over_number,
    cd.ball,
    cd.batsman_runs,
    cd.extra_runs,
    cd.total_runs,
    cd.is_wicket
FROM kbnhzraf_ipl_dwh.curated_deliveries cd
LEFT JOIN kbnhzraf_ipl_dwh.dim_team bt ON cd.batting_team = bt.team_name
LEFT JOIN kbnhzraf_ipl_dwh.dim_player b ON cd.batter = b.player_name
LEFT JOIN kbnhzraf_ipl_dwh.dim_player bw ON cd.bowler = bw.player_name
LEFT JOIN kbnhzraf_ipl_dwh.dim_player f ON cd.fielder = f.player_name;

-- Fact Matches (One row per match)

CREATE TABLE fact_matches (
    match_id INT PRIMARY KEY,
    date_id INT,
    FOREIGN KEY (match_id) REFERENCES kbnhzraf_ipl_dwh.dim_match(match_id),
    FOREIGN KEY (date_id) REFERENCES kbnhzraf_ipl_dwh.dim_date(date_id)
);

INSERT INTO kbnhzraf_ipl_dwh.fact_matches (match_id, date_id)
SELECT
    cm.match_id,
    dd.date_id
FROM kbnhzraf_ipl_dwh.curated_matches cm
LEFT JOIN kbnhzraf_ipl_dwh.dim_date dd ON cm.date = dd.full_date;

-- ==============================================================
-- End of Script
-- ==============================================================
