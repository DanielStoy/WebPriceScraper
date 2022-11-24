import '../css/dashboard.css'
import '../css/common.css'
import { useEffect } from 'react';
import { useState } from 'react';
import { eel } from '../App';

function Dashboard(){
    const [typesOfSites, setTypesOfSites] = useState(['Something'])

    useEffect(() =>{
        eel.getTypes()().then(results =>{
            setTypesOfSites(results)
        });
    }, [])

    return(
        <div className='dashboard'>
            <div className='options'>
                <div className='align-center' id='Search term'>
                    <h3 className='center-text margin-1'>Search Term</h3>
                    <input></input>
                </div>
                <br/>
                <div id='price' className='align-center'>
                    <h3 className='center-text margin-1'>Price</h3>
                    <input className='float-right price-box'></input>
                    <span className='float-right'>-</span>
                    <input className='float-right price-box'></input>
                </div>
                <div className='align-center flex-column' id='typeOfWebsites'>
                    <h3 className='center-text'>Types of Websites to Search</h3>
                    {
                        typesOfSites.map((typeOfSite) =>(
                            <div>
                            <label>{typeOfSite}</label>
                            <input className='float-right' type='checkbox'/>
                            </div>
                        ))
                    }
                </div>
                <button className='submit-button'>Compare</button>
            </div>
        </div>
    )
}



export default Dashboard