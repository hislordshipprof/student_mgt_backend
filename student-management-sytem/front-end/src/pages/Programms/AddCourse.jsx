import React,{useState} from 'react'
import FormInput from '../../components/Form/FormInput';
import Navbar from '../../components/Navbar/Navbar';
import Sidebar from '../../components/Sidebar/Sidebar';
import './ProgramStyle.scss'


const AddCourse = () => {
  const baseUrl = "/api/add_course_save/";
 
  const [values,setValues]=useState('');

   const addCourse = () => {

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
      name: "course_name",
      type: "text",
      placeholder: "Enter Course",
      label: "Course Name",
    },
]



const onChange = (e) => {
  setValues({ ...values, [e.target.name]: e.target.value });
};
const handleSubmit = (e) => {
  e.preventDefault();
  addCourse()
  console.log("data passed succesfully")
  // setValues('')
};

  return (
    <div className="program">
      <Sidebar />
      <div className="programContainer">
        <Navbar />
        <h2>Add Course </h2>
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

            <button type='submit'>Add Course</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default AddCourse