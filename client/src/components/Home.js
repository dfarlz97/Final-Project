import diagram from "./Assets/ADHD.jpg"
import diagram2 from "./Assets/ADHD2.jpg"

export default function Home() {

    const photo_style = {
    width: '50vh',
    height: '50vh'
}
    return (
    <main className="Title">
        <div className ='Home'>
        <h1>About</h1>
        <p>Hello, my name is Lina Farley and I have been practicing Child Pyschology for 10 years.</p>
            {/* <link>Schedule a consultation for your child today!</link> */}
            <div className="photogal">
                <img style={photo_style} src={diagram}></img>
            </div>
        </div>
    </main>
    )
}