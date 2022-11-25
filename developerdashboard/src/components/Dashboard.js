import '../css/dashboard.css'
import '../css/common.css'
import { useEffect } from 'react';
import { useState } from 'react';
import { eel } from '../App';
import Results from './Results';


function Dashboard(){
    const [typesOfSites, setTypesOfSites] = useState([]);
    const [showResults, setShowResults] = useState(false);
    const [priceHigh, setPriceHigh] = useState(0);
    const [priceLow, setPriceLow] = useState(0);
    const [searchTerm, setSearchTerm] = useState('')
    
    useEffect(() =>{
        eel.getTypes()().then(results =>{
            var refinedResult = results.map(x => {
                return {
                    name: x,
                    selected: false
                }
            });
            setTypesOfSites(refinedResult);
        });
    }, [])

    function ComparePrices(){
        setShowResults(true)
    }

    function updateTypes(type, index){
        var typesRefined = typesOfSites;
        typesRefined[index].selected = !type.selected
        setTypesOfSites(typesRefined);
    }

    function updatePriceLow(evt){
        var priceLow = parseFloat(evt.target.value);
        if(isNaN(priceLow)){
            setPriceLow(0);
        }else{
            setPriceLow(priceLow);
            console.log(priceLow)
        }
    }

    function updatePriceHigh(evt){
        var priceHigh = parseFloat(evt.target.value);
        if(isNaN(priceHigh)){
            setPriceHigh(0);
        }else{
            setPriceHigh(priceHigh);
            console.log(priceHigh)
        }
    }

    function updateSearchTerm(evt){
        setSearchTerm(evt.target.value);
    }

    return(
        <div>
            <div>
                {
                    showResults ? <Results priceHigh={priceHigh} priceLow={priceLow} searchTerm={searchTerm} typesOfSites={typesOfSites}/> :

                    <div className='dashboard'>
                    <div className='options'>
                        <div className='align-center' id='Search term'>
                            <h3 className='center-text margin-1'>Search Term</h3>
                            <input className='input-line' onChange={(evt) => updateSearchTerm(evt)}></input>
                        </div>
                        <br />
                        <br />
                        <div id='price' className='align-center'>
                            <h3 className='center-text margin-1'>Price</h3>
                            <input id="priceLow" onChange={(evt) => updatePriceLow(evt)} className=' price-box input-line'></input>
                            <span>-</span>
                            <input id="priceHigh" onChange={(evt) => updatePriceHigh(evt)} className='price-box input-line'></input>
                        </div>
                        <br />
                        <div className='align-center flex-column' id='typeOfWebsites'>
                            <h3 className='center-text'>Types of Websites to Search</h3>
                            {
                                typesOfSites.map((typeOfSite, index) => (
                                    <div>
                                        <label>{typeOfSite.name}</label>
                                        <input className='float-right' type='checkbox' onChange={() => updateTypes(typeOfSite, index) } />
                                    </div>
                                ))
                            }
                        </div>
                        <button className='submit-button' onClick={ComparePrices}>Compare</button>
                    </div>
                </div>
                }
            </div>
        </div>
    )
}



export default Dashboard