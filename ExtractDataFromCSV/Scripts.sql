
drop table message;
DROP TABLE LOGS;

CREATE TABLE message  
    ( message_id      NUMBER   
                     CONSTRAINT message_id_nn NOT NULL 
    ,                CONSTRAINT message_id_pk  
                        PRIMARY KEY (message_id) 
    , message_name    VARCHAR2(25)   
    , message_sql VARCHAR2(500)
    );

CREATE TABLE logs  
    ( log_id      NUMBER   
                     CONSTRAINT log_id_nn NOT NULL 
    ,                CONSTRAINT log_id_pk  
                        PRIMARY KEY (log_id) 
    , log_time    DATE   
    );


INSERT INTO message VALUES   
        ( 1,'XXXX','SELECT log_id FROM logs WHERE log_id=p_key');  

INSERT INTO message VALUES   
        ( 2,'YYYY','SELECT log_id FROM logs WHERE log_id=p_master');  


INSERT INTO logs VALUES   
        ( 1234, TO_DATE('20-02-2020', 'dd-MM-yyyy') );  


INSERT INTO logs VALUES   
        ( 5678, TO_DATE('18-02-2020', 'dd-MM-yyyy') );  
