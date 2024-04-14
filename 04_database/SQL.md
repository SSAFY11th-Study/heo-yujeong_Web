## 1. 개념 및 용어
- 데이터베이스 : 체계적인 데이터 모음
  - 역할 : 데이터를 구조적으로 저장하고 조작 => `CRUD`
- 데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보
- 기존의 데이터 저장 방식
  - 파일(file) : 쉬운 이용, but 어려운 구조적 관리
  - 스프레드 시트(spread sheet) : 행과 열로 구조적 관리
- 관계형 데이터베이스
  - 데이터 간에 관계가 있는 데이터 항목들의 모음
  - 서로 관련된 데이터 포인터를 저장하고, 이에 대한 액세스를 제공
- 관계 : 여러 테이블 간의 `논리적` 연결
- 기본키(primary key) : 데이터의 고유한 식별 값
- 외래키(foreign key) : 데이터의 고유한 식별 값 저장
- 관계형 데이터베이스 관련
  - table(relation) : 데이터를 기록하는 곳
  - field(column, attribute) : 고유한 데이터 형식(타입)이 저장됨
  - record(row, tuple) : 구체적인 데이터 값이 저장됨
  - database(schema) : 테이블의 집합
  - primary key(기본키, pk) : 레코드 식별자
  - foreign key(외래키, fk) : 다른 테이블 간의 관계를 만듦
- DBMS : 데이터베이스를 관리하는 소프트웨어 프로그램
- RDBMS : 관계형 데이터 베이스를 관리하는 소프트웨어 프로그램
  - SQLite, MySQL, PostgreSQL, Oracle Database, ...
- SQL(Structure Query Language)
  - 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
  - 테이블의 형태로 구조화된 관계형 데이터베이스에게 요청을 질의(요청)
  - query : 데이터베이스로부터 정보를 요청
  - syntax : 대소문자 구분 X, 명령어의 마침표 세미콜론(`;`) 필요
  - statements
    | 유형 | 역할 | 키워드 |
    | --- | --- | --- |
    | DDL | 데이터 정의 | CREATE<br>DROP<br>ALTER |
    | DQL | 데이터 검색 | SELECT |
    | DML | 데이터 조작 | INSERT<br>UPDATE<br>DELETE |
    | DCL | 데이터 제어 | COMMIT<br>ROLLBACK<br>GRANT<br>REVOKE |
<br>

## 2. DQL
- SELECT : 선택하려는 필드 지정
  - asterisk(*) 사용하여 모든 필드 선택 가능
- FROM : 데이터 선택하려는 테이블 이름 지정
- WHERE : filtering
  - Clause
    - DISTINCT : 중복제거
    - WHERE : 특정 조건 검색
    - LIMIT
      - LIMIT [offset,] row_count
      - offset => 몇번 이후부터 조회?
      - row_count => 레코드 수
  - Operator
    - BETWEEN
    - IN
    - LIKE
    - Comparison
      - AND(&&), OR(||), NOT(!)
      - `%` : 0개 이상의 문자열과 일치하는지
      - `_` : 단일 문자
    - Logical
- GROUP BY : 레코드를 그룹화하여 요약본 생성(집계함수와 함께 사용) - aggregation
  - SUM, AVG, MAX, MIN, COUNT
- HAVING : 집계항목에 대한 세부 조건
- ORDER BY : 데이터 정렬
  - ASC : 오름차순
  - DESC : 내림차순
- 실행 순서
  - FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
<br>

## 3. DDL
```SQL
-- 테이블 생성
CREATE TABLE 테이블명(
  컬럼명 데이터타입 제약조건,
  컬럼명 데이터타입 제약조건
);
```
- 데이터타입
  - NULL, INTEGER, REAL, TEXT, BLOB(이미지, 동영상, 문서 등의 바이너리 데이터)
- 제약조건(constraints) : 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장
  - PRIMARY KEY
  - NOT NULL
  - FOREIGN KEY
  - + AUTHOINCREMENT

```SQL
-- 스키마 확인
PRAGMA table_info('테이블명');
```

```SQL
-- 테이블 추가
-- 1. 필드 추가
ALTER TABLE 테이블명 ADD COLUMN 컬럼명 데이터타입 제약조건;
-- 2. 필드 이름 변경
ALTER TABLE 테이블명 RENAME COLUMN 컬럼명 TO 새컬럼명;
-- 3. 테이블 이름 변경
ALTER TABLE 테이블명 RENAME TO 새테이블명;
```

```SQL
-- 테이블 삭제
DROP TABLE 테이블명;
```
<br>

## 4. DML
```SQL
-- 데이터 추가
INSERT INTO 테이블명(컬럼명, 컬럼명, ...)
VALUES (값, 값, ...);
```

```SQL
-- 데이터 수정
UPDATE 테이블명
SET 컬럼명 = 값 [, 컬럼명 = 값]
[WHERE condition];
```

```SQL
-- 데이터 삭제
DELETE FROM 테이블명 [WHERE condition];
```
<br>

## 5. JOIN
- INNER JOIN
  - 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
```SQL
FROM 메인테이블 INNER JOIN 조인할테이블 ON 조인할테이블.fk = 메인테이블.pk;
```
- LEFT JOIN
  - 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
  - 매칭되는 레코드 없으면 NULL 표시
```SQL
FROM 왼쪽테이블 LEFT JOIN 오른쪽테이블 ON 오른쪽테이블.fk = 왼쪽테이블.pk;
```