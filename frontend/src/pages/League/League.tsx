import React from "react";
import { useParams } from "react-router-dom";
import LeagueForm from "../../components/LeagueForm/LeagueForm";
import LeagueDashboard from "../../components/LeagueDashboard/LeagueDashboard";
import './League.scss'

function League() {
  const {idFromParams} = useParams()

  return (
    <>
      <h1>League Page</h1>
      {!idFromParams ? <LeagueForm /> : <LeagueDashboard />}
    </>
  );
};

export default League;
