// eslint-disable-next-line react/prop-types
export default function UserBox({name, password, id}) {
    return (
        <article>
            <h3>{id}</h3>
            <h3>{name}</h3>
            <p>{password}</p>
        </article>
    )
}