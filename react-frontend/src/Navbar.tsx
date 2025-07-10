import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar () {
    return(
        <>
        <nav className="navbar">
            <div className="navbar-content">
                <Link to="/"><h1>League Papi</h1></Link>
            </div>
        </nav>
        </>
    )

}
export default Navbar