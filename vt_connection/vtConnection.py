import json
import sqlalchemy as db
import logging

db_host="localhost"
db_port="5432"
db_name="iskur_db"
db_user="admin1"
db_password="123"

try:
    engine = db.create_engine(
        'postgresql://' + db_user + ':' + db_password + '@' + db_host + ':' + db_port + '/' + db_name)
    session = engine.connect()
    employee = db.Table('employee', db.MetaData(), autoload=True, autoload_with=engine)
    firm = db.Table('firm', db.MetaData(), autoload=True, autoload_with=engine)
    unemployed = db.Table('unemployed', db.MetaData(), autoload=True, autoload_with=engine)
    interview = db.Table('interview', db.MetaData(), autoload=True, autoload_with=engine)
    todo = db.Table('todo', db.MetaData(), autoload=True, autoload_with=engine)
    logging.basicConfig()
    logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.INFO)

    print("Connected Db: " + db_name)
except Exception as e:
    print("NoConnectionDb: ", e)


def type_cast_to_dict(data):
    if data is None:
        return None
    elif type(data) == list:
        result_list = []
        for item in data:
            result_list.append(dict(item))
        return result_list
    else:
        return dict(data)


# employees db --->
def readEmployees():
    readEmployees_sql = db.select([employee, firm.c.name_.label("firm_name")]).select_from(employee.join(firm,employee.c.firm_id == firm.c.id))
    
    print('\nSQLAlchemy:', readEmployees_sql.compile(compile_kwargs={"literal_binds": True}))
    data = session.execute(readEmployees_sql).fetchall()
    print("3",data)
    print(type_cast_to_dict(data))
    return type_cast_to_dict(data)


def filterAndReadEmployees(filterType, filterValue):
    # filterType: 'id', 'name' -> string
    # returning data should be: {'employees': [json_object, json_object2, json_object3, ...]}
    if filterType == 'experience':
        filterAndReadEmployees_sql = db.select([employee, firm.c.name_]).select_from(employee.join(firm,
                                                                                                   employee.c.firm_id == firm.c.id)).where(
            employee.c[filterType] >= int(filterValue))
    else:
        filterAndReadEmployees_sql = db.select([employee, firm.c.name_]).select_from(employee.join(firm,
                                                                                                   employee.c.firm_id == firm.c.id)).where(
            employee.c[filterType].like("%" + filterValue + "%"))

    data = type_cast_to_dict(session.execute(filterAndReadEmployees_sql).fetchall())
    print(data)
    return data


# unemployeds db --->
# data: array of unemployeds
def readUnemployeds():
    readEmployees_sql = unemployed.select()
    data = session.execute(readEmployees_sql).fetchall()
    return type_cast_to_dict(data)


def filterAndReadUnemployeds(filterType, filterValue):
    # filterType: 'id', 'name' -> string
    # returning data should be: {'firms': [json_object, json_object2, json_object3, ...]}
    if filterType != 'experience':
        filterAndReadUnemployeds_sql = unemployed.select().where(unemployed.c[filterType].like("%" + filterValue + "%"))
        data = type_cast_to_dict(session.execute(filterAndReadUnemployeds_sql).fetchall())
    else:
        filterAndReadUnemployeds_sql = unemployed.select().where(unemployed.c[filterType] >= filterValue)
        data = type_cast_to_dict(session.execute(filterAndReadUnemployeds_sql).fetchall())
    return data

def unemployedInfoShow(ssn):
    filterAndReadUnemployeds_sql = unemployed.select().where(unemployed.c.ssn==ssn)
    data = type_cast_to_dict(session.execute(filterAndReadUnemployeds_sql).fetchone())
    return data


def addNewUnemployed(data):
    try:
        session.execute(db.insert(unemployed), data)
        return print('Başvuru eklendi.')
    except Exception as e:
        print(e)
        return print('Hata: Başvuru eklenemedi.')


def updateUnemployed(data):
    # update unemployed
    # ssn cannot change
    # find the update row with ssn
    updateUnemployed_sql = db.update(unemployed).where(unemployed.c.ssn == data['ssn'])
    session.execute(updateUnemployed_sql, data)

    print(data)



# data should be: {'firms': [json_object, json_object2, json_object3, ...]}
def readFirms():
    readFirms_sql = firm.select()
    data = session.execute(readFirms_sql).fetchall()
    print(type_cast_to_dict(data))
    return type_cast_to_dict(data)


def filterAndReadFirms(filterType, filterValue):
    # filterType: 'id', 'name' -> string
    # returning data should be: {'firms': [json_object, json_object2, json_object3, ...]}
    if filterType == 'id':
        filterAndReadFirms_sql = firm.select().where(firm.c[filterType] == filterValue)
    else:
        filterAndReadFirms_sql = firm.select().where(firm.c[filterType].like('%' + filterValue + '%'))
    data = session.execute(filterAndReadFirms_sql).fetchall()
    return type_cast_to_dict(data)


# data: firm single json_object
def addNewFirm(data):
    try:
        session.execute(db.insert(firm), data)
        return print('Firma eklendi.')
    except Exception as e:
        print(e)
        return print('Hata: Firma eklenemedi.')


# deletes plural firms by id
# deleteFirmList: [0, 2, 1, 75, ...] -> integer ids
def deleteWithIdFirm(deleteFirmId):
    deleteWithIdFirm_sql = db.delete(firm).where(firm.c.id == deleteFirmId)
    session.execute(deleteWithIdFirm_sql)
    return print('Firma Silindi.')


def updateFirm(data):
    updateFirm_sql = db.update(firm).where(firm.c.id == data['id'])
    session.execute(updateFirm_sql, data)
    return print('Firma Güncellendi')


# interview db --->
def readAllInterviews():
    
    data = session.execute("select * from view_1").fetchall()
    return type_cast_to_dict(data)


def filterAndReadAllInterviews(filterType, filterValue):
    if filterType == 'id':
        readInterviews_sql = db.select(
            [interview, firm.c.name_.label('firm_name'), unemployed.c.name_.label("worker_name")]) \
            .select_from(interview.join(firm, interview.c.firm_id == firm.c.id).join(unemployed, interview.c.worker_ssn
                                                                                     == unemployed.c.ssn)).where(
            interview.c.id == int(filterValue))
    elif filterType == 'worker_name':
        readInterviews_sql = db.select(
            [interview, firm.c.name_.label('firm_name'), unemployed.c.name_.label("worker_name")]) \
            .select_from(interview.join(firm, interview.c.firm_id == firm.c.id).join(unemployed, interview.c.worker_ssn
                                                                                     == unemployed.c.ssn)).where(
            unemployed.c.name_.like('%' + filterValue + '%'))
    else:
        readInterviews_sql = db.select(
            [interview, firm.c.name_.label('firm_name'), unemployed.c.name_.label("worker_name")]) \
            .select_from(interview.join(firm, interview.c.firm_id == firm.c.id).join(unemployed, interview.c.worker_ssn
                                                                                     == unemployed.c.ssn)).where(
            firm.c.name_.like('%' + filterValue + '%'))

    data = session.execute(readInterviews_sql).fetchall()
    return type_cast_to_dict(data)


def readNullInterviews():
    readInterviews_sql = db.select([interview, firm.c.name_.label('firm_name'),
                                    unemployed.c.name_.label("worker_name")]).select_from(
        interview.join(firm, interview.c.firm_id == firm.c.id).join(
            unemployed, interview.c.worker_ssn == unemployed.c.ssn)).where(interview.c.outcome == None)
    print('\nSQLAlchemy:', readInterviews_sql.compile(compile_kwargs={"literal_binds": True}))
    data = session.execute(readInterviews_sql).fetchall()
    return type_cast_to_dict(data)


def filterAndReadNullInterviews(filterType, filterValue):
    if filterType == 'id':
        readInterviews_sql = db.select(
            [interview, firm.c.name_.label('firm_name'), unemployed.c.name_.label("worker_name")]) \
            .select_from(interview.join(firm, interview.c.firm_id == firm.c.id).join(unemployed, interview.c.worker_ssn
                                                                                     == unemployed.c.ssn)).where(
            db.and_(interview.c.id == int(filterValue), interview.c.outcome == None))
    elif filterType == 'worker_name':
        readInterviews_sql = db.select(
            [interview, firm.c.name_.label('firm_name'), unemployed.c.name_.label("worker_name")]) \
            .select_from(interview.join(firm, interview.c.firm_id == firm.c.id).join(unemployed, interview.c.worker_ssn
                                                                                     == unemployed.c.ssn)).where(
            db.and_(unemployed.c.name_.like('%' + filterValue + '%'), interview.c.outcome == None))
    else:
        readInterviews_sql = db.select(
            [interview, firm.c.name_.label('firm_name'), unemployed.c.name_.label("worker_name")]) \
            .select_from(interview.join(firm, interview.c.firm_id == firm.c.id).join(unemployed, interview.c.worker_ssn
                                                                                     == unemployed.c.ssn)).where(
            db.and_(unemployed.c.name_.like('%' + filterValue + '%'), interview.c.outcome == None))

    data = session.execute(readInterviews_sql).fetchall()
    return type_cast_to_dict(data)


def createNewInterview(interviews):
    try:
        session.execute(db.insert(interview), interviews)
        return 'Mülakatlar oluşturuldu.'
    except Exception as e:
        return 'Hata: Mülakatlar oluşturulamadı!!!:'+str(e)


def listUnemployedsByRequirementsOfFirm(firms_id: int,isBekar,isErkek,tecrube,startdate,enddate):
    firm_attributes_sql=db.select([firm]).where(firm.c.id==firms_id)
    firm_attributes = session.execute(firm_attributes_sql).fetchone()
    egitim=firm_attributes["req_grad_level"]
    engel=firm_attributes["disable_permission"]
    sicil=firm_attributes["registery_permission"]

    unemployed_list_sql=db.select([unemployed]).where(db.and_(unemployed.c.marriage==isBekar,
                                                             unemployed.c.gender==isErkek,
                                                             unemployed.c.experience>=tecrube,
                                                             unemployed.c.birthdate.between(startdate, enddate),
                                                             unemployed.c.grad_level==egitim ,
                                                             unemployed.c.disable_level == (not engel),
                                                             unemployed.c.registery == (not sicil)
                                                            )
                                                    )

    #print('\nSQLAlchemy:', unemployed_list_sql.compile(compile_kwargs={"literal_binds": True}))
    data = session.execute(unemployed_list_sql).fetchall()
    return type_cast_to_dict(data)
    # Firmanın minimum istekleri doğrultusunda bir unemployed listesi dönmeli

#########################################################################################
#########################################################################################

def total_salary(firm_id: int):
    data = session.execute("select total_salary("+str(firm_id)+")").fetchall()
    return type_cast_to_dict(data)


def hireOrDenyUnemployed(hired_unemployed_ssn: str, hiring_firm_id: int, outcome: bool, maas: int):
    if outcome:
        #tmp_employee = type_cast_to_dict(session.execute(db.select([unemployed]).where(unemployed.c.ssn==hired_unemployed_ssn)).fetchone())
        #session.execute(db.insert(employee),tmp_employee)
        session.execute(interview.update().where(db.and_(interview.c.worker_ssn==hired_unemployed_ssn, interview.c.firm_id==hiring_firm_id)).values(outcome=outcome))
        session.execute(employee.update().where(employee.c.ssn==hired_unemployed_ssn).values(salary=maas))
        session.execute("select hire_employee_firm('"+hired_unemployed_ssn+"')").fetchall()
    else:
        session.execute(interview.update().where(db.and_(interview.c.worker_ssn==hired_unemployed_ssn, interview.c.firm_id==hiring_firm_id)).values(outcome=outcome))

def deleteWithSsnUnemployed(deleteUnemployed):
    print('Silinen SSN: ', deleteUnemployed)
    deleteWithSsnUnemployed_sql = db.delete(unemployed).where(unemployed.c.ssn == deleteUnemployed)
    session.execute(deleteWithSsnUnemployed_sql)
    # session.execute("select delete_unemployed('"+deleteUnemployed+"')")

def avg_age():
    data= session.execute("select avg(extract(year from age(CURRENT_DATE,birthdate))) from unemployed").fetchall()
    return type_cast_to_dict(data)

def hires_from_firm(min_employee_count: int):
    if min_employee_count == 0:
        data = readFirms()
    else:
        data= session.execute("select * from firm f2 where f2.id in (SELECT firm_id FROM interview where outcome = "
                            "True GROUP BY firm_id HAVING count(firm_id)>="+str(min_employee_count)+")").fetchall()
    return type_cast_to_dict(data)


def readTodos():
    readTodos_sql = todo.select()
    data = session.execute(readTodos_sql).fetchall()
    return type_cast_to_dict(data)

def addTodo(todo_):
    todo_ = {'todo': todo_}
    try:
        session.execute(db.insert(todo), todo_)
        return None
    except Exception as e:
        return e

def deleteTodo(todoText):
    deleteTodo_sql = db.delete(todo).where(todo.c.todo == todoText)
    session.execute(deleteTodo_sql)


