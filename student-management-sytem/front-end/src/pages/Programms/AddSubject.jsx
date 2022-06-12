import React,{useState,useEffect} from 'react'
import FormInput from '../../components/Form/FormInput';

import Navbar from '../../components/Navbar/Navbar';
import Sidebar from '../../components/Sidebar/Sidebar';
import './ProgramStyle.scss'
const AddSubject = () => {
const baseUrl = "/api/add_subject";
const baseUrl2 = "/api/add_subject_save/";

const [mydata, setMydata] = useState([]); 
    
const [values, setValues] = useState({

  subject_name: "",
  course_id:"1",
  staff_id:"1"
});


const addSubject = () => {
     fetch(baseUrl2, {
       method: "POST",
       headers: {
         "Content-Type": "application/json",
       },
       body: JSON.stringify(values),

     })
       .then((response) =>  response.json())
      
       //Then with the data from the response in JSON...
       .then((data) => {
         console.log("Success:", data);
         setValues(data);
         
         
       })

       //Then with the error genereted...
       .catch((error) => {
         console.error("Error:", error);
       });
      
   };
   


 useEffect(() => {
   fetch(baseUrl)
     .then((response) => response.json())
     .then((mydata) => {
       console.log("here is mydata", mydata);
       setMydata(mydata);
     });
 }, []); 

const inputs = [
  {
    id: 1,
    name: "subject_name",
    type: "text",
    placeholder: "Enter Subject",
    label: "Subject Name",
   
  },
  
];


const onChange = (e) => {
  setValues({ ...values, [e.target.name]: e.target.value });
};


const handleSubmit = (e) => {
  e.preventDefault();
  addSubject()
 
};
     

  return (
    <div className="program">
      <Sidebar />
      <div className="programContainer">
        <Navbar />
     
        <h2>Add Subject </h2>
        <div className="Formfield">
          <form onSubmit={handleSubmit}>
            {inputs.map((input) => (
              <FormInput
                key={input.id}
                {...input}
                value={values[input.name]}
                onChange={onChange}
              />
            ))}
            <select  name="course_id" onChange={onChange}>
              {mydata?.courses?.map((course) => (
                <option  name="course_id" value={course.id} key={course.id}>
                  Course:{`${course.course_name}`}
                </option>
              ))}
            </select>
            <select name="staff_id" onChange={onChange}>
              {mydata?.staffs?.map((staff) => (
                <option name="staff_id" value={staff.id} key={staff.id}>
                  Staff: {`${staff.first_name}`}
                </option>
              ))}
            </select>

            <button type="submit">Add Subject</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default AddSubject