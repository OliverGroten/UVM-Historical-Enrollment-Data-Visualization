# UVM-Historical-Enrollment-Data-Visualization

The goal of this project is twofold:
1. Create an interactive visualization of UVM enrollment data going back to 1995
2. Commit to and finish a project outside of the stucture of school.

Project Specifications:
- Have users interact with a web interface in which they can graph and manipulate variables relating to UVM's enrollment data
- Scrape this data from the web and store it in an SQL database
- Use some kind of graphing library for JavaScript to handle the graph components
- Make it a refined product

Database Schema:

SUBJECTS TABLE

| id | subject | f_key |
|----|--------:|-------|
| 01 | CS008   | 1     |    
| 02 | CS021   | 0     |
| 03 | CS124   | 2     |
| 04 | CS202   | 3     |
| 05 | CS148   | 1     |

CLASS TABLE

| id | teacher | year | f_key |
|----|--------:|------|-------|
| 01 | Bob     | 2017 | 1     |
| 02 | Bob     | 2018 | 1     |
| 03 | Lisa    | 2017 | 2     |
| 04 | Lisa    | 2018 | 2     |
| 05 | Joe     | 2021 | 3     |

Schema Notes: 
- The foreign key (f_key) is generated with the Class table based on the teacher (where each teacher has a unique foreign key)
- The ID column on each table is independent of the foreign key
- The second row in subjects (CS021) uses f_key of `0` as a placeholder for another teacher not shown in the Class table

The theory behind this schema is that the Subjects table will be relatively static with only a small change (if any) each year. The Class table on the other hand will only increase by the number of classes offered for that semester. This should result in an efficient database that is easily referenced.
