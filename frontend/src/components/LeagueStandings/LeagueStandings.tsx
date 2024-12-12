import React, { useState, useEffect } from "react";
import "./LeagueStandings.scss";
import axios from "axios";
import LeagueCalendar from "../LeagueCalendar/LeagueCalendar";

const { REACT_APP_SERVER_URL } = process.env;

interface InputsProps {
  leagueId: any;
}

function LeagueStandings({ leagueId }: InputsProps) {
  const [teams, setTeams] = useState<any>(null);
  const [games, setGames] = useState<any>(null);

  const getTeams = async () => {
    const response = await axios.get(`${REACT_APP_SERVER_URL}/teams`);

    setTeams(response.data.filter((team:any) => (
      team["League"] === leagueId
    )));
  };

  const getGames = async () => {
    const response = await axios.get(
      `${REACT_APP_SERVER_URL}/games/league/${leagueId}`
    );

    setGames(response.data);
  };

  useEffect(() => {
    getTeams();
    getGames();
  }, [leagueId]);

  if (!teams || !games) {
    return <p>Loading....</p>;
  }

  const leagueTeams = teams.filter((team: any) => team["League"] === leagueId);

  return (
    <>
      <table>
        <thead>
          <tr>
            <th className="team-column">Team</th>
            <th>Wins</th>
            <th>Losses</th>
            <th>Winning %</th>
          </tr>
        </thead>
        <tbody>
          {leagueTeams.map((team: any) => (
            <tr key={team["TeamId"]}>
              <td className="team-column">{team["TeamName"]}</td>
              <td className="table-data">
                {
                  games.filter(
                    (wins: any) => team["TeamId"] === wins["WinningTeamId"]
                  ).length
                }
              </td>
              <td className="table-data">
                {games.filter(
                  (game: any) =>
                    team["TeamId"] === game["HomeTeamId"] ||
                    team["TeamId"] === game["VisitingTeamId"]
                ).length -
                  games.filter(
                    (wins: any) => team["TeamId"] === wins["WinningTeamId"]
                  ).length}
              </td>
              <td className="table-data">
                {(
                  Number(
                    games.filter(
                      (wins: any) => team["TeamId"] === wins["WinningTeamId"]
                    ).length || 0
                  ) /
                    games.filter(
                      (game: any) =>
                        team["TeamId"] === game["HomeTeamId"] ||
                        team["TeamId"] === game["VisitingTeamId"]
                    ).length || 0
                )
                  .toFixed(3)
                  .replace(/^0+/, "")}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <div>
        <LeagueCalendar games={games} leagueTeams={leagueTeams} />
      </div>
    </>
  );
}

export default LeagueStandings;
