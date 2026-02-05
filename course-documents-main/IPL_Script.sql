DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.fact_matches;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.fact_deliveries;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.curated_deliveries;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.curated_matches;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_team;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_player;
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_match;

DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_date
DROP TABLE IF EXISTS kbnhzraf_ipl_dwh.dim_venue;


CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_db.match_info (
    match_number INT PRIMARY KEY,
    team1 VARCHAR(100) NOT NULL,
    team2 VARCHAR(100) NOT NULL,
    match_date DATE NOT NULL,
    toss_winner VARCHAR(100),
    toss_decision ENUM('bat', 'field') NOT NULL,
    result VARCHAR(20),
    eliminator VARCHAR(100), -- Can store 'NA', 'Yes', 'No', etc.
    winner VARCHAR(100),
    player_of_match VARCHAR(100),
    venue VARCHAR(255),
    city VARCHAR(100),
    team1_players TEXT, -- List of players (comma-separated)
    team2_players TEXT  -- List of players (comma-separated)
);

CREATE TABLE kbnhzraf_ipl_db.deliverables (
    match_id INT NOT NULL,
    inning INT NOT NULL,
    over_num INT NOT NULL,
    ball_num INT NOT NULL,
    batter VARCHAR(50),
    bowler VARCHAR(50),
    non_striker VARCHAR(50),
    extras_type VARCHAR(20),
    batsman_runs INT,
    extra_runs INT,
    total_runs INT,
    is_wicket TINYINT(1),
    player_dismissed VARCHAR(50),
    dismissal_kind VARCHAR(50),
    fielder VARCHAR(50),
    batting_team VARCHAR(50),
    PRIMARY KEY (match_id, inning, over_num, ball_num)
);


-- Load CSV files into the deliverables and match_info Tables

--Filter only 2025 records and store into another tables

CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_db.match_info_2025 AS
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
FROM kbnhzraf_ipl_db.match_info
WHERE YEAR(match_date) = 2025;


CREATE TABLE IF NOT EXISTS kbnhzraf_ipl_db.deliveries_2025 AS
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
FROM kbnhzraf_ipl_db.deliverables
WHERE match_id IN (SELECT match_id FROM kbnhzraf_ipl_db.match_info_2025);

DELETE FROM kbnhzraf_ipl_db.match_info
WHERE YEAR(match_date) = 2025;

DELETE FROM kbnhzraf_ipl_db.deliverables
WHERE match_id IN (SELECT match_id FROM kbnhzraf_ipl_db.match_info_2025)