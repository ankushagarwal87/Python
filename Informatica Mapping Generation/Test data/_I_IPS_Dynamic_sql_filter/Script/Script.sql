
--------------------------------------------------------
--  DDL for Source Table DIM_COUNTRIES
--------------------------------------------------------

  CREATE TABLE "DIM_COUNTRIES" 
   (	
    "COUNTRY_KEY" NUMBER, 
	"COUNTRY_CODE" VARCHAR2(20 BYTE), 
	"COUNTRY_ISO_CODE" CHAR(2 CHAR), 
	"COUNTRY_NAME" VARCHAR2(40 CHAR), 
	"COUNTRY_SUBREGION" VARCHAR2(30 CHAR), 
	"COUNTRY_REGION" VARCHAR2(20 CHAR), 
	"COUNTRY_TOTAL" VARCHAR2(11 CHAR), 
	"COUNTRY_NAME_HIST" VARCHAR2(40 CHAR), 
	"INSERT_DT" DATE, 
	"LAST_UPDATE_DT" DATE, 
	"DW_INSERT_DT" DATE, 
	"DW_UPDATE_DT" DATE, 
	"MD5_CHECKSUM" VARCHAR2(32 CHAR), 
	"CDC_FLAG" VARCHAR2(1 CHAR)
   );
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (1,'CNTRY-52790','US','United States of America','Northern America','Americas','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (2,'CNTRY-52776','DE','Germany','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (3,'CNTRY-52789','GB','United Kingdom','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (4,'CNTRY-52784','NL','The Netherlands','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (5,'CNTRY-52780','IE','Ireland','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (6,'CNTRY-52777','DK','Denmark','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (7,'CNTRY-52779','FR','France','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (8,'CNTRY-52778','ES','Spain','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (9,'CNTRY-52788','TR','Turkey','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (10,'CNTRY-52786','PL','Poland','Eastern Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (11,'CNTRY-52775','BR','Brazil','Southern America','Americas','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (12,'CNTRY-52773','AR','Argentina','Southern America','Americas','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (13,'CNTRY-52783','MY','Malaysia','Asia','Asia','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (14,'CNTRY-52782','JP','Japan','Asia','Asia','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (15,'CNTRY-52781','IN','India','Asia','Asia','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (16,'CNTRY-52774','AU','Australia','Australia','Oceania','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (17,'CNTRY-52785','NZ','New Zealand','Australia','Oceania','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (18,'CNTRY-52791','ZA','South Africa','Africa','Africa','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (19,'CNTRY-52787','SA','Saudi Arabia','Middle East','Middle East','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (20,'CNTRY-52772','CA','Canada','Northern America','Americas','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (21,'CNTRY-52771','CN','China','Asia','Asia','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (22,'CNTRY-52769','SG','Singapore','Asia','Asia','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);
Insert into DIM_COUNTRIES (COUNTRY_KEY,COUNTRY_CODE,COUNTRY_ISO_CODE,COUNTRY_NAME,COUNTRY_SUBREGION,COUNTRY_REGION,COUNTRY_TOTAL,COUNTRY_NAME_HIST,INSERT_DT,LAST_UPDATE_DT,DW_INSERT_DT,DW_UPDATE_DT,MD5_CHECKSUM,CDC_FLAG) values (23,'CNTRY-52770','IT','Italy','Western Europe','Europe','World total',null,to_date('31-MAY-14','DD-MON-RR'),to_date('31-MAY-14','DD-MON-RR'),to_date('27-JAN-15','DD-MON-RR'),null,null,null);

commit;

--------------------------------------------------------
--  DDL for Target Table COUNTRIES_DETAILS
--------------------------------------------------------

  CREATE TABLE "COUNTRIES_DETAILS" 
   (	"COUNTRY_KEY" NUMBER, 
	"COUNTRY_CODE" VARCHAR2(20 BYTE), 
	"COUNTRY_ISO_CODE" CHAR(2 CHAR), 
	"COUNTRY_NAME" VARCHAR2(40 CHAR), 
	"COUNTRY_SUBREGION" VARCHAR2(30 CHAR), 
	"COUNTRY_REGION" VARCHAR2(20 CHAR), 
	"COUNTRY_TOTAL" VARCHAR2(11 CHAR), 
	"COUNTRY_NAME_HIST" VARCHAR2(40 CHAR), 
	"INSERT_DT" DATE, 
	"LAST_UPDATE_DT" DATE, 
	"DW_INSERT_DT" DATE, 
	"DW_UPDATE_DT" DATE, 
	"MD5_CHECKSUM" VARCHAR2(32 CHAR), 
	"CDC_FLAG" VARCHAR2(1 CHAR)
   ); 