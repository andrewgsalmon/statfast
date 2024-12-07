import React, { useState, useEffect } from "react";
import axios from "axios";

interface InputsProps {
  leagueId: any;
}

function LeagueStandings({ leagueId }: InputsProps) {
  const [teams, setTeams] = useState<any>(null);

  const getTeams = async () => {
    const response = await axios.get("http://localhost:8000/teams");

    setTeams(response.data);
  };

  useEffect(() => {
    getTeams();
  }, [leagueId]);

  if (!teams) {
    return <p>Loading....</p>;
  }

  const leagueTeams = teams.filter((team: any) => team["League"] === leagueId);

  return (
    <table>
      <tr>
        <th>Team</th>
        <th>Wins</th>
        <th>Losses</th>
        <th>Winning %</th>
      </tr>
      {leagueTeams.map((team: any) => (
        <tr>
          <td>{team["TeamName"]}</td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      ))}
    </table>
  );
}

export default LeagueStandings;
