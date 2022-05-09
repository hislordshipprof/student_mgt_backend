import React,{useState,useEffect} from 'react'
import FormInput from '../../components/Form/FormInput';
import Navbar from '../../components/Navbar/Navbar';
import Sidebar from '../../components/Sidebar/Sidebar';
import './AddStaff.scss'



const AddStaff = () => {
  const baseUrl = "/api/add_staff_save/";



  const [values, setValues] = useState({
    username: "",
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    password2:"",
    address: "",
  });


  const sendData= async()=>{
    //POST request with body equal on data in JSON format
    // const toSend={
    //   ...values,
    //   password2:'password2'.values
    // }
    // try {
    //   const res = await fetch(baseUrl, {
    //     method: "POST",
    //     headers: {
    //       "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify(values),
    //   });
    //   res.json().then((rex)=>console.log('ttt',rex))
    //   return res.json();
    // } catch (error) {
    //   console.log('error',error)
    // }


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
  }



  
  const inputs = [
    {
      id: 1,
      name: "username",
      type: "text",
      placeholder: "User Name",
      label: "User Name",
      required: true,
      errorMessage:
        "Username should be 3-16 characters and shouldnt include any special character!",
    },
    {
      id: 2,
      name: "email",
      type: "email",
      placeholder: "Email",
      label: "Email",
      errorMessage: "It should be a valid email address!",
      required: true,
    },
    {
      id: 3,
      name: "password",
      type: "password",
      placeholder: "Password",
      label: "Password",
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
      label: "First Nmae",
    },

    {
      id: 6,
      name: "last_name",
      type: "text",
      placeholder: "Last Name",
      label: "Last Name",
    },

    {
      id: 7,
      name: "address",
      type: "text",
      placeholder: "Address",
      label: "Address",
    },
  ];




  const onChange = (e) => {
    setValues({ ...values, [e.target.name]: e.target.value });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    sendData()
    console.log('mydata',values)
  };
  return (
    <div className="stafflist">
      <Sidebar />
      <div className="stafflistContainer">
        <Navbar />

        <h2>Add Staff </h2>
        <div className="Formfield">
          <form onSubmit={handleSubmit}>
            <h1>Add Staff</h1>
            {inputs.map((input) => (
              <FormInput
                key={input.id}
                {...input}
                value={values[input.name]}
                onChange={onChange}
              />
            ))}

            <button type='submit' >Add Staff</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default AddStaff