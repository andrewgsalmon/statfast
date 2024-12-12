import React, { useState, useEffect } from 'react'
import './LeagueCalendar.scss'

import { useCalendarApp, ScheduleXCalendar } from "@schedule-x/react";
import {
  createViewMonthAgenda,
  createViewMonthGrid,
} from "@schedule-x/calendar";
import { createEventModalPlugin } from '@schedule-x/event-modal'
import { createEventsServicePlugin } from "@schedule-x/events-service";
import "@schedule-x/theme-default/dist/index.css";

type Team = {
  TeamId: number;
  TeamName: string;
  HomeField: string;
}

type Game = {
  HomeTeamId: number;
  VisitingTeamId: number;
  GameId: number;
  Date: string;
}

interface InputsProps {
  games: Game[];
  leagueTeams: Team[];
}

function LeagueCalendar({games, leagueTeams}: InputsProps) {

  let gameArray = games.map((game: Game) => {
    const homeTeam: Team | undefined = leagueTeams.find((team:Team) => team.TeamId === game.HomeTeamId);
    const visitingTeam: Team | undefined = leagueTeams.find((team:Team) => team.TeamId === game.VisitingTeamId);

    return {
      id: game.GameId,
      title: `${visitingTeam?.TeamName ?? "Unknown"} @ ${homeTeam?.TeamName ?? "Unknown"}`,
      location: `${homeTeam?.HomeField ?? "Unknown"}`,
      start: game.Date.replace(/[A-Z]/gi, " ").slice(0, -4),
      end: game.Date.replace(/[A-Z]/gi, " ").slice(0, -4),
    }
  })

  const eventsService = useState(() => createEventsServicePlugin())[0];

  const eventModal = createEventModalPlugin()

  const calendar = useCalendarApp({
    views: [
      createViewMonthGrid(),
      createViewMonthAgenda(),
    ],
    events: gameArray,
    plugins: [eventsService, eventModal],
    // callbacks: {
    //   onEventClick(calendarEvent:any) {
    //     window.location.href = 'https://www.mlb.com';
    //   },
    // },
    firstDayOfWeek: 0,
  });

  eventModal.close();

  useEffect(() => {
      // get all events
      eventsService.getAll();
  }, [games]);

  return (
    <ScheduleXCalendar calendarApp={calendar} />
  )
}

export default LeagueCalendar