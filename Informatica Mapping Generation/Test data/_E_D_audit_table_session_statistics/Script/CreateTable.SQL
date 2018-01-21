--------------------------------------------------------
-- Create Source table
--------------------------------------------------------

DROP TABLE EMPLOYEE_SRC;

CREATE TABLE EMPLOYEE_SRC
(
  EMPLOYEE_ID  NUMBER ,
  FIRST_NAME   VARCHAR2(25 BYTE),
  LAST_NAME    VARCHAR2(25 BYTE),
  PHONE_NO     NUMBER
);

INSERT INTO EMPLOYEE_SRC (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, PHONE_NO) VALUES ('1', 'Martin', 'Taylor', '256566');
INSERT INTO EMPLOYEE_SRC (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, PHONE_NO) VALUES ('2', 'Richard', 'May', '56897');
INSERT INTO EMPLOYEE_SRC (FIRST_NAME, LAST_NAME, PHONE_NO) VALUES ('Albert', 'Jackson', '111445');
INSERT INTO EMPLOYEE_SRC (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, PHONE_NO) VALUES ('4', 'Raphel', 'Sheldon', '887744');
INSERT INTO EMPLOYEE_SRC (FIRST_NAME, LAST_NAME, PHONE_NO) VALUES ('Anna', 'Seles', '34567');

COMMIT;
--------------------------------------------------------
-- Create target table
--------------------------------------------------------
DROP TABLE EMPLOYEE;

CREATE TABLE EMPLOYEE
(
  EMPLOYEE_ID  NUMBER   NOT NULL,
  FIRST_NAME   VARCHAR2(25 BYTE),
  LAST_NAME    VARCHAR2(25 BYTE),
  PHONE_NO     NUMBER
);

--------------------------------------------------------
-- Insert data into target table
-------------------------------------------------------

INSERT INTO EMPLOYEE (EMPLOYEE_ID, FIRST_NAME, LAST_NAME) VALUES ('1', 'Martin', 'Taylor');

Commit;
