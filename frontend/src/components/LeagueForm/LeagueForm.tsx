import React, {useState} from 'react'

function LeagueForm() {
  const [league, setLeague] = useState<Number | null>(null)

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()

    console.log(league)
  }

  const handleLeagueSelect = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setLeague(Number(e.target.value));
  };

  return (
    <form className="league__form" onSubmit={handleSubmit}>
        <select onChange={handleLeagueSelect} name="league" id="league__select">
          <option>--</option>
          <option value="1">COBA</option>
          <option value="2">OUA</option>
        </select>
        <button type="submit">Go to my league</button>
      </form>
  )
}

export default LeagueForm