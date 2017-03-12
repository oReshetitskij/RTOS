import random
import string
import datetime

databaseFilePath = 'hotelDB.sqlite3'

databaseDropOrCreateQuery  = """PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Clients
DROP TABLE IF EXISTS Clients;

CREATE TABLE Clients (
    Id           INTEGER PRIMARY KEY AUTOINCREMENT,
    Name         TEXT    NOT NULL,
    Passport     TEXT    NOT NULL,
    CheckInDate  DATE    NOT NULL,
    CheckOutDate DATE    NOT NULL
                         CHECK (CheckInDate < CheckOutDate),
    RoomId       INTEGER REFERENCES Rooms (Id)
                         NOT NULL,
    Service1     INTEGER REFERENCES Services (Id),
    Service2     INTEGER REFERENCES Services (Id),
    Service3     INTEGER REFERENCES Services (Id),
    Price        DECIMAL NOT NULL,
    EmployeeId   INTEGER REFERENCES Employees (Id)
);


-- Table: Employees
DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees (
    Id         INTEGER PRIMARY KEY AUTOINCREMENT,
    Name       TEXT    NOT NULL,
    Age        INTEGER NOT NULL,
    Sex        TEXT    NOT NULL,
    Address    TEXT    NOT NULL,
    Passport   TEXT    NOT NULL,
    PositionId INTEGER NOT NULL
                       REFERENCES Positions (Id)
);


-- Table: Positions
DROP TABLE IF EXISTS Positions;

CREATE TABLE Positions (
    Id               INTEGER PRIMARY KEY AUTOINCREMENT,
    Name             TEXT    NOT NULL,
    Sallary          DECIMAL NOT NULL,
    Responsibilities TEXT    NOT NULL,
    Requirements     TEXT    NOT NULL
);


-- Table: Rooms
DROP TABLE IF EXISTS Rooms;

CREATE TABLE Rooms (
    Id          INTEGER PRIMARY KEY AUTOINCREMENT,
    Name        TEXT    NOT NULL,
    Capacity    INTEGER NOT NULL,
    Description TEXT    NOT NULL,
    Price       DECIMAL NOT NULL,
    EmployeeId          REFERENCES Employees (Id) ON DELETE SET NULL
);


-- Table: Services
DROP TABLE IF EXISTS Services;

CREATE TABLE Services (
    Id          INTEGER PRIMARY KEY AUTOINCREMENT,
    Name        TEXT    NOT NULL,
    Description TEXT    NOT NULL,
    Price       DECIMAL NOT NULL
);


-- Index:
DROP INDEX IF EXISTS "";

CREATE INDEX "" ON Employees (
    Id
);


-- View: ClientsView
DROP VIEW IF EXISTS ClientsView;
CREATE VIEW ClientsView AS
    SELECT *
      FROM Clients
           JOIN
           RoomsView ON RoomsView.EmployeeId == Clients.EmployeeId
           JOIN
           Services ON Services.Id == Clients.Service1
           JOIN
           Services AS Services2 ON Services2.Id == Clients.Service2
           JOIN
           Services AS Services3 ON Services3.Id == Clients.Service3;


-- View: HRDepartmentView
DROP VIEW IF EXISTS HRDepartmentView;
CREATE VIEW HRDepartmentView AS
    SELECT Employees.Id,
           Employees.Name,
           Employees.Age,
           Employees.Sex,
           Employees.Address,
           Employees.Passport,
           Positions.Name AS PositionName,
           Positions.Sallary,
           Positions.Responsibilities,
           Positions.Requirements
      FROM Employees
           JOIN
           Positions ON Employees.PositionId == Positions.Id;


-- View: RoomsView
DROP VIEW IF EXISTS RoomsView;
CREATE VIEW RoomsView AS
    SELECT Employees.Id AS EmployeeId,
           Employees.Name,
           Employees.Age,
           Employees.Sex,
           Employees.Address,
           Employees.Passport,
           Employees.PositionId,
           Rooms.Id AS RoomId,
           Rooms.Name AS RoomName,
           Rooms.Capacity,
           Rooms.Description,
           Rooms.Price
      FROM Employees
           JOIN
           Rooms ON Rooms.EmployeeId == Employees.Id;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;"""

def fillDatabase(conn):
    # add positions to the DB
    positions = [('Front Desk Clerks', 1000, 'Accounting, Active Listening, Administrative',
                  'Assists with treatment ordered by physician as supervised by physician or registered nurse. Performs select clinical duties.'),
                 ('Waiter', 1200, 'Analytical, Behavioral, Blue Collar Job Skills',
                  'Performs basic clerical duties including answering phones, maintaining records, and filing'),
                 ('Kitchen Staff', 1500, 'Business Intelligence, Business',
                  'Performs basic material management function to include ordering and stocking of supplies. Assists with maintaining a clean and orderly environment'),
                 ('Supervisor', 2400, 'Consulting, Content Strategy, Creative Thinking, Critical Thinking',
                  'Works with the center staff to coordinate patient flow and to assure that operations are working smoothly. Pulls patient charts.'),
                 ('Hotel Manager', 5000, 'Customer Service, Decision Making, Delegation, Deductive Reasoning',
                  'Work collaboratively with key stakeholders to determine areas of optimization, deconstruct issues and develop solution approach')]
    conn.executemany('INSERT INTO Positions (Name, Sallary, Responsibilities, Requirements) Values(?,?,?,?)', positions)

    # add employees to the DB
    employees = []
    names = ["Andrii A. V.", "Andrey R. V.", "Alex D. K.", "Ivan S. V.", "Bogdan K. A.", "Kiril S. U.", "Lesia A. K.",
             "Dima S. S.", "Nadia A. P.", "Andrii A. S."]
    for employeeId in range(1, 11):
        employees.append(
            (names[employeeId - 1], random.randint(18, 60), random.randint(0, 1), "address", id_generator(7),
             random.randint(1, 5)))
    conn.executemany('INSERT INTO Employees (Name, Age, Sex, Address, Passport, PositionId)  VALUES (?,?,?,?,?,?)',
                     employees)

    # add rooms to the DB
    rooms = []
    for roomsId in range(1, 11):
        rooms.append(
            ("Room #" + str(roomsId), random.randint(2, 6), "Amazing room", random.randint(200, 1000),
             random.randint(1, 10)))
    conn.executemany('INSERT INTO Rooms (Name, Capacity, Description, Price, EmployeeId) VALUES (?,?,?,?,?)', rooms)

    services = [("Dinner", "Description", 80),
                ("Supper", "Description", 60),
                ("Breakfast", "Description", 35),
                ("Wi-fi", "Description", 20),
                ("Hot water", "Description", 100)]
    conn.executemany('INSERT INTO Services (Name, Description, Price) VALUES (?,?,?)', services)

    clients = []
    for clientId in range(1, 21):
        visitYear = random.randint(2013, 2017)
        start_date = datetime.date.today().replace(day=1, month=1, year=visitYear).toordinal()
        end_date = datetime.date.today().replace(day=1, month=1, year=visitYear + 1).toordinal()
        checkInDate = datetime.date.fromordinal(random.randint(start_date, end_date))
        visitDuration = random.randint(3, 20)
        checkOutDate = checkInDate + datetime.timedelta(days=visitDuration)
        clients.append(("Client" + str(clientId), id_generator(7), checkInDate.strftime('%m/%d/%Y'),
                        checkOutDate.strftime('%m/%d/%Y'), random.randint(1, 10),
                        random.randint(1, 5), random.randint(1, 5), random.randint(1, 5),
                        random.randint(1000, 3000) * visitDuration,
                        random.randint(1, 10)))
    conn.executemany(
        'INSERT INTO Clients (Name, Passport, CheckInDate, CheckOutDate, RoomId, Service1, Service2, Service3, Price, EmployeeId) VALUES (?,?,?,?,?,?,?,?,?,?)',
        clients)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))