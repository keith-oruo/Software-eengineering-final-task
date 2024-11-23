CREATE DATABASE CustomerFeedbackDB;

USE CustomerFeedbackDB;

CREATE TABLE CustomerFeedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    FeedbackText TEXT NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
