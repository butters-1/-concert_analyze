-- Data Vault 2.0 tables for Ticketmaster event data

-- Hubs
CREATE TABLE IF NOT EXISTS hub_event (
    event_id VARCHAR PRIMARY KEY,
    load_date TIMESTAMP,
    record_source VARCHAR
);

CREATE TABLE IF NOT EXISTS hub_venue (
    venue_id VARCHAR PRIMARY KEY,
    load_date TIMESTAMP,
    record_source VARCHAR
);

-- Links
CREATE TABLE IF NOT EXISTS link_event_venue (
    event_id VARCHAR,
    venue_id VARCHAR,
    load_date TIMESTAMP,
    record_source VARCHAR,
    PRIMARY KEY (event_id, venue_id),
    FOREIGN KEY (event_id) REFERENCES hub_event(event_id),
    FOREIGN KEY (venue_id) REFERENCES hub_venue(venue_id)
);

-- Satellites
CREATE TABLE IF NOT EXISTS sat_event_details (
    event_id VARCHAR,
    load_date TIMESTAMP,
    record_source VARCHAR,
    name VARCHAR,
    start_date DATE,
    start_time TIME,
    timezone VARCHAR,
    PRIMARY KEY (event_id, load_date),
    FOREIGN KEY (event_id) REFERENCES hub_event(event_id)
);

CREATE TABLE IF NOT EXISTS sat_venue_details (
    venue_id VARCHAR,
    load_date TIMESTAMP,
    record_source VARCHAR,
    venue_name VARCHAR,
    city VARCHAR,
    state VARCHAR,
    country VARCHAR,
    PRIMARY KEY (venue_id, load_date),
    FOREIGN KEY (venue_id) REFERENCES hub_venue(venue_id)
);
