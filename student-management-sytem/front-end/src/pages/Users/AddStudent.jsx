import React, { useState,useEffect } from "react";
import FormInput from "../../components/Form/FormInput";
import Navbar from "../../components/Navbar/Navbar";
import Sidebar from "../../components/Sidebar/Sidebar";
import "./AddStudent.scss";

const AddStudent = () => {
   const baseUrl = "/api/add_student_save/";

   const baseUrl2 = "http://127.0.0.1:8000/api/manage_course/";
  const[mydata,setMydata]=useState([
  ]) 
  const [values, setValues] = useState({
    username: "",
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    password2:"",
    address: "",
    // course_id:"",
    gender:"",
    profile_pic:"",
  });
 
 useEffect(() => {
  
   fetch(baseUrl2)
     .then((response) => response.json())
     .then((mydata) => {
       console.log(mydata);
       console.log("m=------dada", mydata);
       setMydata(mydata);
     });
  
 }, []); 
   
  

   const addStudent = () => {
     fetch(baseUrl, {
       method: "POST",
       headers: {
         "Content-Type": "application/json",
       },
       body: JSON.stringify(values),
     })
       .then((response) => response.json())
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

  const inputs = [
    {
      id: 1,
      name: "username",
      type: "text",
      placeholder: "User Name",
      label: "User Name:",
      required: true,
      errorMessage:
        "Username should be 3-16 characters and shouldnt include any special character!",
     oder1:'order1'
    },
    {
      id: 2,
      name: "email",
      type: "email",
      placeholder: "Email",
      label: "Email:",
      errorMessage: "It should be a valid email address!",
      required: true,
     
    },
    {
      id: 3,
      name: "password",
      type: "password",
      placeholder: "Password",
      label: "Password:",
      errorMessage:
        "Password should be 8-20 characters and include at least 1 letter,1 number and 1 special character@##!",
      pattern: `^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$`,
      required: true,
     
    },
    {
      id: 4,
      name: "password2",
      type: "password",
      placeholder: "Confirm Password",
      label: "Confirm Password",
      errorMessage:
        "Password should be 8-20 characters and include at least 1 letter,1 number and 1 special character@##!",
      pattern: `^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$`,
      required: true,
     
    },
    {
      id: 5,
      name: "first_name",
      type: "text",
      placeholder: "First Name",
      label: "First Nmae:",
      
    },

    {
      id: 6,
      name: "last_name",
      type: "text",
      placeholder: "Last Name",
      label: "Last Name:",
      
    },

    {
      id: 7,
      name: "address",
      type: "text",
      placeholder: "Address",
      label: "Address:",
      
    },
    {
      id: 8,
      name: "course_id",
      type: "text",
      placeholder: "choice",
      label: "Course:",
      
    },
  
    {
      id: 9,
      name: "session year",
      type: "date",
      placeholder: "",
      label: "Session Year",
      
    },

    {
      id: 10,
      name: "gender",
      type: "text",
      placeholder: "male",
      label: "Sex",
     
    },

    {
      id: 11,
      name: "profile_pic",
      type: "file",
      placeholder: "",
      label: "Profile Pic",
      
    },
  ];

  
  const onChange = (e) => {
    setValues({ ...values, [e.target.name]: e.target.value });
    
  };


  const handleSubmit = (e) => {
    e.preventDefault();
    addStudent()

  };
  console.log("first", mydata?.courses);
  return (
    <div className="studentlist">
      <Sidebar />
      <div className="studentlistContainer">
        <Navbar />

        <h2>Add Student </h2>
        <div className="Formfield">
          <form onSubmit={handleSubmit}>
            <h1>Add Student</h1>
            {inputs.map((input) => (
              <FormInput
                key={input.id}
                {...input}
                value={values[input.name]}
                onChange={onChange}
                
                
              />
            ))}
           
            <select >
            
              {mydata?.courses?.map((course) => (
               
            <option value={course.id} key={course.id} onChange={(e) => setMydata(e.target.value)}>{course.course_name} </option>       
              ))}
            </select>
                  
            <button type="submit">Add Student</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default AddStudent;
