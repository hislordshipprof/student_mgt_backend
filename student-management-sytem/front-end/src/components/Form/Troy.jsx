import React,{useState} from 'react'

const Troy = () => {
    const [form,setForm]=useState({
        name:"",
        email:"",
        country:"Togo"
    })


    const updateData=(e)=>{
        setForm({...form,[e.target.name]:e.target.value})
    }
    const showData=()=>{
    console.log('first',form)
    
    }
    const onSubmit=(e)=>{
        e.preventDefault()
    }
    const input=([
        {id:1,
        name:'ghana'},
        {id:2,
        name:'cameroon'},
        {id:3,
        name:'Togo'},

    ])
  return (
    <div>
      <form onSubmit={onSubmit}>
        <label>
          Username:
          <input name="name" onChange={updateData} value={form.name} />
        </label>
        <br />
        <hr />
        <label>
          Email:
          <input name="email" onChange={updateData} value={form.email} />
        </label>
        <label>
          select:
          <select name="country" onChange={updateData} value={form.country}>
            {input.map((inputs) => (
              <option key={inputs.id} value={inputs.name}>{inputs.name}</option>
            ))}
          </select>
        </label>
        <div>
          <button onClick={showData}>submit</button>
        </div>
      </form>
    </div>
  );
}

export default Troy