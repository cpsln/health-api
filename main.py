
from app import app
from sign import signupDoctor   
from login import loginDoctor
from create_patient import CreatPatient
import contact
from patientAlternateCoctact import FillAlternateContact
from patientList import PatientList
from getPatientData import patientData
import editPersonal
import editProfile
import careTeamMember
import forgotPassword
# import changePassword
# import createMessage
# import billing
# import contactDoc
# import doctorAternateContact
# import doctorData
# import addVital



if __name__ == '__main__':
#    app.run(debug = True)
    app.secret_key = 'some secret key'
    app.debug = True
    app.run(host='0.0.0.0',port=5001)