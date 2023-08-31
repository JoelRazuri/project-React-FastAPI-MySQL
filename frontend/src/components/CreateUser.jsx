export default function CreateUser() {
    return (
        <form>
            <label htmlFor="name">Name:</label>
            <input id="name" type="text"/>
            <label htmlFor="passwrod">Password:</label>
            <input id="password" type="password"/>
            <input type="submit" value={CreateUser}/>
        </form>
    )
}