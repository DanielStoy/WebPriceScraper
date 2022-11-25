import { useEffect } from 'react';
import { useState } from 'react';
import { eel } from '../App';
import '../css/results.css';
import '../css/common.css';


function Results(props){
    const [sites, setSites] = useState([]);
    useEffect(() => {
        var priceLow = "";
        var priceHigh = "";
        var types = [];
        if(props.priceLow != 0 && props.priceHigh != 0 ){
            priceLow = props.priceLow.toString();
            priceHigh = props.priceHigh.toString();
        }
        props.typesOfSites.forEach(element => {
            if(element.selected){
                types.push(element.name);
            }
        });
        eel.getAveragePrices(priceLow, priceHigh, props.searchTerm, types)().then((results) => {
            setSites(results);
        })
    }, [])

    return(
        <div>
            <h2 className='center-text'>Prices</h2>
            <div id='resultsContainer' className='result-container flex-column'>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Average Price</th>
                    <th>Amount Of Products</th>
                </tr>
                {
                    sites.map((site, index) => (
                        <tr>
                            <td>{site.name}</td>
                            <td>{site.averagePrice}</td>
                            <td>{site.amountOfPrices}</td>
                        </tr>
                    ))
                }
            </table>
            </div>
        </div>
    )
}

/*<div>
<span className='result-header float-left'>Name</span>
<span className='result-header float-right'>Avg.Price .... Amount of Products</span>
</div>
{
sites.map((site, index) => (
    <div>
        <span className='float-left result'>{site.name}</span>
        <span className='float-right result'>{site.averagePrice}$ .... {site.amountOfPrices}</span>
    </div>
))
} */

export default Results