import {React, useState} from 'react'
import Home from './Home'
import { Link } from "react-router-dom";

export default function Start(){

    const [open, setOpen] = useState(false)

    const MODAL_STYLES = {
    position: 'fixed',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    backgroundColor: '#FFF',
    padding: '50px',
    zIndex: 1000,
    width: '25vh',
    height: '15vh'
}

const OVERLAY_STYLES = { 
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0,0,0,.75)',
    zIndex: 1000,
}

    function handleClickOpen(){
        setOpen(!open)
    }

    if (open){
        return(
            <Home />
        )
    }

    return(
        <div style={OVERLAY_STYLES}>
            <div style={MODAL_STYLES}>
                <Link className="modalLink" to='/signup'>Login or Signup to Continue.</Link>
                <button class="glow-on-hover" onClick = {handleClickOpen}>Close</button>
            </div>
     
        </div>
    )
}