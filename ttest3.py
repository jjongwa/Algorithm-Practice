SELECT M.ID, M.NAME, COUNT(M.ID)
from MERCHANTS M, CARD_USAGES C
where LOCATE("강남", M.NAME) or LOCATE("논현", M.NAME) and M.ID = C.MERCHANT_ID
group by M.ID
order by M.ID


SELECT round(avg(T_A.AGE))
from TOSS_AGE_GENDER T_A
where AGE != "NULL"



select IFNULL(AGE, 34) AGE
from TOSS_AGE_GENDER T



-- 코드를 입력하세요

SELECT TOSS.GENDER, TOSS.tri, COUNT(TOSS.ID)
FROM(SELECT *, case 
                    when AGE <20 and GENDER = "남자" then "20대 미만"
                    when AGE <20 and GENDER = "여자" then "20대 미만"
                    when (AGE >=20 and AGE <30) and GENDER = "남자" then "20대 이상 30대 미만"
                    when (AGE >=20 and AGE <30) and GENDER = "여자" then 4
                    when (AGE >=30 and AGE <40) and GENDER = "남자" then 5
                    when (AGE >=30 and AGE <40) and GENDER = "여자" then 6
                    when (AGE >=40 and AGE <50) and GENDER = "남자" then 7
                    when (AGE >=40 and AGE <50) and GENDER = "여자" then 8
                    when (AGE >=50 and AGE <60) and GENDER = "남자" then 9
                    when (AGE >=50 and AGE <60) and GENDER = "여자" then 10
                    when AGE >=60 and GENDER = "남자" then 11
                    when AGE >=60 and GENDER = "여자" then 12
            else 222
            end tri
    FROM (SELECT TM.ID, TM.BOARD_ID, TM.USER_ID, GG.AGE, GG.GENDER
            from TOSS_COMMUNITY_MESSAGE TM
            join (SELECT NEW_A.USER_ID, NEW_A.AGE, NEW_A.GENDER 
                from(   SELECT T.ID, T.USER_ID, IFNULL(T.AGE, TA.AAGE) AGE, T.GENDER
                        FROM TOSS_AGE_GENDER T
                        join(   SELECT round(avg(T_A.AGE)) AAGE
                                from TOSS_AGE_GENDER T_A
                                where AGE != "NULL")TA) NEW_A
                join TOSS_USER TU on TU.ID = NEW_A.USER_ID
                where TU.TRADE_YN = 'Y') GG on TM.USER_ID = GG.USER_ID) TTT) TOSS
GROUP BY tri, GENDER
ORDER BY COUNT(TOSS.ID) desc
