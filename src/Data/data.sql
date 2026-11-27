CREATE DATABASE gawab CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE gawab;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  role ENUM('donor','charity','admin') NOT NULL,
  name VARCHAR(120) NOT NULL,
  national_id CHAR(14) NULL,         
  phone VARCHAR(20),
  address VARCHAR(255),
  email VARCHAR(150) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  is_verified BOOLEAN DEFAULT FALSE,  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE donation_posts (          
  id INT AUTO_INCREMENT PRIMARY KEY,
  donor_id INT NOT NULL,
  category VARCHAR(30) NOT NULL,
  title VARCHAR(150) NOT NULL,
  details JSON,                        
  photo_path VARCHAR(255),
  location VARCHAR(255),
  status ENUM('Draft','Available','Claimed','Accepted') DEFAULT 'Available',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (donor_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE claims (
  id INT AUTO_INCREMENT PRIMARY KEY,
  post_id INT NOT NULL,
  charity_id INT NOT NULL,
  status ENUM('Claimed','Accepted','Rejected') DEFAULT 'Claimed',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (post_id) REFERENCES donation_posts(id) ON DELETE CASCADE,
  FOREIGN KEY (charity_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE campaigns (
  id INT AUTO_INCREMENT PRIMARY KEY,
  charity_id INT NOT NULL,
  title VARCHAR(150) NOT NULL,
  category VARCHAR(30),
  description TEXT,
  goal DECIMAL(12,2) NOT NULL,
  raised DECIMAL(12,2) DEFAULT 0,
  deadline DATE,
  status ENUM('Pending approval','Active','Rejected') DEFAULT 'Pending approval',
  FOREIGN KEY (charity_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE money_donations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  donor_id INT NOT NULL,
  campaign_id INT NOT NULL,
  amount DECIMAL(12,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (donor_id) REFERENCES users(id),
  FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);

CREATE TABLE volunteer_opportunities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  charity_id INT NOT NULL,
  title VARCHAR(150), category VARCHAR(30), description TEXT,
  needed INT, when_text VARCHAR(100), location VARCHAR(255),
  FOREIGN KEY (charity_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE volunteer_applications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  opportunity_id INT NULL,
  volunteer_id INT NOT NULL,
  date DATE, hours VARCHAR(30), area VARCHAR(255), note TEXT,
  status ENUM('Pending','Accepted','Rejected') DEFAULT 'Pending',
  FOREIGN KEY (opportunity_id) REFERENCES volunteer_opportunities(id) ON DELETE CASCADE,
  FOREIGN KEY (volunteer_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE announcements (
  id INT AUTO_INCREMENT PRIMARY KEY,
  charity_id INT NOT NULL,
  title VARCHAR(150), message TEXT,
  event_date DATE, location VARCHAR(255),
  campaign_id INT NULL, needs VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (charity_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE notifications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  title VARCHAR(150), message VARCHAR(255), link VARCHAR(50),
  is_read BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);