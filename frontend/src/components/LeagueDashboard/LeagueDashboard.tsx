import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import LeagueStandings from "../LeagueStandings/LeagueStandings";

function LeagueDashboard() {
  const [league, setLeague] = useState<any>(null);

  const { idFromParams } = useParams();

  const leagueDetails = async (leagueId: any) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/leagues/${leagueId}`
      );

      setLeague(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    leagueDetails(idFromParams);
  }, [idFromParams]);

  if (!league) {
    return <p>Loading...</p>;
  }

  return (
    <>
      <h2>{league["LeagueName"]}</h2>
      <LeagueStandings leagueId={league["LeagueId"]}/>
    </>
  );
}

export default LeagueDashboard;
