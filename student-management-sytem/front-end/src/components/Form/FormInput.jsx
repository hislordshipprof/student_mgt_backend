import React,{useState} from 'react'
import './FormInput.scss'
const FormInput = (props) => {
    const {label,errorMessage,onChange,id,order1,order2,...inputProps}=props;
    const[focused,setFocused]=useState(false);

    const handleFocus=(e)=>{
      setFocused(true)
    }
  return (
    <div className="forminput">
      <label>{label}</label>
      <input
        {...inputProps}
        onChange={onChange}
        onBlur={handleFocus}
        focused={focused.toString()}
      />
   

      <span>{errorMessage}</span>
    </div>
//     <div className="forminput">
//       <label>{label}</label>
//      {order1?( <input
//         {...inputProps}
//         onChange={onChange}
//         onBlur={handleFocus}
//         focused={focused.toString()}
//       />
//      ): order2?(
//       <select {...inputProps}>
//         <option value="A">{onchange}</option>
        
//       </select>):null
// }
//       <span>{errorMessage}</span>


// allow audio call
//ya der?
// am here

// well which page are we working on 

//its der
//     </div>
  );
}

export default FormInput