import { LoaderFunctionArgs } from '@remix-run/node';
import {
  type ClientLoaderFunctionArgs,
  Link,
  MetaFunction,
  Params,
  useLoaderData,
} from '@remix-run/react';
import { useMemo } from 'react';

import BiCalendar from '~icons/bi/calendar';
import BiGraphUp from '~icons/bi/graph-up';
import BiInfoCircleFill from '~icons/bi/info-circle-fill';
import BiLink from '~icons/bi/link';
import BiListOl from '~icons/bi/list-ol';
import BiPinMapFill from '~icons/bi/pin-map-fill';
import BiTrophy from '~icons/bi/trophy';
import MdiFolderMediaOutline from '~icons/mdi/folder-media-outline';
import MdiGraphBoxOutline from '~icons/mdi/graph-box-outline';
import MdiRobot from '~icons/mdi/robot';
import MdiTournament from '~icons/mdi/tournament';

import {
  Award,
  Event,
  Match,
  Media,
  Team,
  getEvent,
  getEventAlliances,
  getEventAwards,
  getEventMatches,
  getEventRankings,
  getEventTeamMedia,
  getEventTeams,
} from '~/api/v3';
import AllianceSelectionTable from '~/components/tba/allianceSelectionTable';
import AwardRecipientLink from '~/components/tba/awardRecipientLink';
import InlineIcon from '~/components/tba/inlineIcon';
import MatchResultsTable from '~/components/tba/matchResultsTable';
import RankingsTable from '~/components/tba/rankingsTable';
import { Badge } from '~/components/ui/badge';
import { Card } from '~/components/ui/card';
import {
  Credenza,
  CredenzaBody,
  CredenzaClose,
  CredenzaContent,
  CredenzaDescription,
  CredenzaFooter,
  CredenzaHeader,
  CredenzaTitle,
  CredenzaTrigger,
} from '~/components/ui/credenza';
import { ScrollArea } from '~/components/ui/scroll-area';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '~/components/ui/tabs';
import { sortAwardsComparator } from '~/lib/awardUtils';
import { getEventDateString, isValidEventKey } from '~/lib/eventUtils';
import { sortMatchComparator } from '~/lib/matchUtils';
import { getTeamPreferredRobotPicMedium } from '~/lib/mediaUtils';
import { sortTeamKeysComparator, sortTeamsComparator } from '~/lib/teamUtils';

async function loadData(params: Params) {
  if (params.eventKey === undefined) {
    throw new Error('Missing eventKey');
  }

  if (!isValidEventKey(params.eventKey)) {
    throw new Response(null, {
      status: 404,
    });
  }

  const [event, matches, alliances, rankings, awards, teams, teamMedia] =
    await Promise.all([
      getEvent({ eventKey: params.eventKey }),
      getEventMatches({ eventKey: params.eventKey }),
      getEventAlliances({ eventKey: params.eventKey }),
      getEventRankings({ eventKey: params.eventKey }),
      getEventAwards({ eventKey: params.eventKey }),
      getEventTeams({ eventKey: params.eventKey }),
      getEventTeamMedia({ eventKey: params.eventKey }),
    ]);

  if (event.status == 404) {
    throw new Response(null, {
      status: 404,
    });
  }

  if (
    event.status !== 200 ||
    matches.status !== 200 ||
    alliances.status !== 200 ||
    rankings.status !== 200 ||
    awards.status !== 200 ||
    teams.status !== 200 ||
    teamMedia.status !== 200
  ) {
    throw new Response(null, {
      status: 500,
    });
  }

  return {
    event: event.data,
    matches: matches.data,
    alliances: alliances.data,
    rankings: rankings.data,
    awards: awards.data,
    teams: teams.data,
    teamMedia: teamMedia.data,
  };
}

export async function loader({ params }: LoaderFunctionArgs) {
  return await loadData(params);
}

export async function clientLoader({ params }: ClientLoaderFunctionArgs) {
  return await loadData(params);
}

export const meta: MetaFunction<typeof loader> = ({ data }) => {
  return [
    { title: `${data?.event.name} (${data?.event.year}) - The Blue Alliance` },
    {
      name: 'description',
      content: `Videos and match results for the ${data?.event.year} ${data?.event.name} FIRST Robotics Competition.`,
    },
  ];
};

export default function EventPage() {
  const { event, alliances, matches, rankings, awards, teams, teamMedia } =
    useLoaderData<typeof loader>();

  const sortedMatches = useMemo(
    () => matches.sort(sortMatchComparator),
    [matches],
  );

  const quals = useMemo(
    () => sortedMatches.filter((m) => m.comp_level === 'qm'),
    [sortedMatches],
  );

  const elims = useMemo(
    () => sortedMatches.filter((m) => m.comp_level !== 'qm'),
    [sortedMatches],
  );

  const leftSideMatches =
    matches.length > 0 ? (
      <>
        <h2 className="text-xl">
          {quals.length > 0 ? 'Quals' : 'Elims'} Results
        </h2>
        <MatchResultsTable
          matches={quals.length > 0 ? quals : elims}
          event={event}
        />
      </>
    ) : null;

  const rightSideElims =
    quals.length > 0 && elims.length > 0 ? (
      <>
        <h2 className="mt-4 text-xl">Playoff Results</h2>
        <MatchResultsTable matches={elims} event={event} />
      </>
    ) : null;

  return (
    <div className="py-8">
      <h1 className="mb-3 text-3xl font-medium">
        {event.name} {event.year}
      </h1>

      <InlineIcon>
        <BiCalendar />
        {getEventDateString(event, 'long')}
        {event.week !== null && (
          <Badge className="mx-2 h-[1.5em] align-text-top">
            Week {event.week + 1}
          </Badge>
        )}
      </InlineIcon>

      <InlineIcon>
        <BiPinMapFill />

        {event.gmaps_url ? (
          <Link to={event.gmaps_url}>
            {event.city}, {event.state_prov}, {event.country}
          </Link>
        ) : (
          <>
            {event.city}, {event.state_prov}, {event.country}
          </>
        )}
      </InlineIcon>
      {event.website && (
        <InlineIcon>
          <BiLink />
          <Link to={event.website}>{event.website}</Link>
        </InlineIcon>
      )}

      {event.first_event_code && (
        <InlineIcon>
          <BiInfoCircleFill />
          Details on{' '}
          <Link
            to={`https://frc-events.firstinspires.org/${event.year}/${event.first_event_code}`}
          >
            FRC Events
          </Link>
        </InlineIcon>
      )}

      <InlineIcon>
        <BiGraphUp />
        <Link to={`https://www.statbotics.io/event/${event.key}`}>
          Statbotics
        </Link>
      </InlineIcon>

      <Tabs
        defaultValue={matches.length > 0 ? 'results' : 'teams'}
        className="mt-4"
      >
        <TabsList
          className="flex h-auto flex-wrap items-center justify-evenly [&>*]:basis-1/2
            lg:[&>*]:basis-1"
        >
          {(matches.length > 0 || (alliances && alliances.length > 0)) && (
            <TabsTrigger value="results">
              <InlineIcon>
                <MdiTournament />
                Results
              </InlineIcon>
            </TabsTrigger>
          )}
          {rankings && rankings.rankings.length > 0 && (
            <TabsTrigger value="rankings">
              <InlineIcon>
                <BiListOl />
                Rankings
              </InlineIcon>
            </TabsTrigger>
          )}
          {awards.length > 0 && (
            <TabsTrigger value="awards">
              <InlineIcon>
                <BiTrophy />
                Awards
              </InlineIcon>
            </TabsTrigger>
          )}
          <TabsTrigger value="teams">
            <InlineIcon>
              <MdiRobot />
              Teams
              <Badge className="mx-2 h-[1.5em] align-text-top" variant="inline">
                {teams.length}
              </Badge>
            </InlineIcon>
          </TabsTrigger>
          <TabsTrigger value="insights">
            <InlineIcon>
              <MdiGraphBoxOutline />
              Insights
            </InlineIcon>
          </TabsTrigger>
          <TabsTrigger value="media">
            <InlineIcon>
              <MdiFolderMediaOutline />
              Media
            </InlineIcon>
          </TabsTrigger>
        </TabsList>

        <TabsContent value="results">
          <div className="flex flex-wrap gap-4 lg:flex-nowrap">
            <div className="basis-full lg:basis-1/2">{leftSideMatches}</div>

            <div className="basis-full lg:basis-1/2">
              {alliances && (
                <AllianceSelectionTable
                  alliances={alliances}
                  year={event.year}
                />
              )}
              {rightSideElims}
            </div>
          </div>
        </TabsContent>

        {rankings && (
          <TabsContent value="rankings">
            <RankingsTable
              rankings={rankings}
              winners={
                alliances?.find((a) => a.status?.status === 'won')?.picks ?? []
              }
            />
          </TabsContent>
        )}

        <TabsContent value="awards">
          <AwardsTab awards={awards} />
        </TabsContent>

        <TabsContent value="teams">
          <TeamsTab
            teams={teams}
            matches={sortedMatches}
            event={event}
            media={teamMedia}
          />
        </TabsContent>

        <TabsContent value="insights">insights</TabsContent>

        <TabsContent value="media">media</TabsContent>
      </Tabs>
    </div>
  );
}

function AwardsTab({ awards }: { awards: Award[] }) {
  awards.sort(sortAwardsComparator);
  return (
    <div className="flex flex-wrap-reverse">
      <div className="mt-1 flow-root w-full">
        <dl className="divide-y divide-gray-100 text-sm">
          {awards.map((award) => (
            <div
              key={award.name}
              className="grid grid-cols-1 gap-1 py-2 sm:grid-cols-3 sm:gap-4 sm:px-10"
            >
              <dt className="font-medium text-gray-900 sm:col-span-2">
                {award.name}
              </dt>
              <dd className="text-gray-700 sm:text-right">
                {award.recipient_list
                  .sort((a, b) =>
                    sortTeamKeysComparator(
                      a.team_key ?? '0',
                      b.team_key ?? '0',
                    ),
                  )
                  .map((r, i) => [
                    i > 0 && (r.awardee ? <br /> : ', '),
                    <AwardRecipientLink
                      recipient={r}
                      key={`${award.award_type}-${r.awardee}-${r.team_key}`}
                      year={award.year}
                    />,
                  ])}
              </dd>
            </div>
          ))}
        </dl>
      </div>
    </div>
  );
}

function TeamsTab({
  teams,
  matches,
  event,
  media,
}: {
  teams: Team[];
  matches: Match[];
  event: Event;
  media: Media[];
}) {
  teams.sort(sortTeamsComparator);

  // todo
  // 1. add hover effects
  // 2. split out CredenzaTrigger, so the same UI (Body) can be triggered by different UI elements
  return (
    <div className="md:columns-2">
      {teams.map((t) => (
        <Credenza key={t.key}>
          <CredenzaTrigger asChild>
            <Card className="content-visibility-auto my-0 mb-1 flex h-[150px] cursor-pointer items-center gap-4 rounded-lg bg-background p-4">
              <div className="grid flex-1 gap-1">
                <div className="font-medium">
                  {t.team_number} - {t.nickname}
                </div>
                <div className="text-sm text-muted-foreground">
                  {t.city}, {t.state_prov}, {t.country}
                </div>
              </div>
              {(() => {
                const maybeImage = getTeamPreferredRobotPicMedium(
                  media.filter((m) => m.team_keys.includes(t.key)),
                );

                return maybeImage === undefined ? null : (
                  <img
                    src={maybeImage}
                    alt={`${t.team_number}'s robot`}
                    className="h-full w-1/3 rounded-lg border-2 border-neutral-300 object-cover"
                    loading="lazy"
                  />
                );
              })()}
            </Card>
          </CredenzaTrigger>
          <CredenzaContent>
            <CredenzaHeader>
              <CredenzaTitle>
                {t.team_number} - {t.nickname} at {event.short_name}
              </CredenzaTitle>
              <CredenzaDescription>
                From {t.city}, {t.state_prov}, {t.country}
              </CredenzaDescription>
            </CredenzaHeader>
            <CredenzaBody>
              <ScrollArea className="h-[70vh] md:h-auto">
                <MatchResultsTable
                  team={t}
                  matches={matches.filter(
                    (m) =>
                      m.alliances.blue.team_keys.includes(t.key) ||
                      m.alliances.red.team_keys.includes(t.key),
                  )}
                  event={event}
                />
              </ScrollArea>
            </CredenzaBody>
            <CredenzaFooter>
              <CredenzaClose asChild>
                <button>Close</button>
              </CredenzaClose>
            </CredenzaFooter>
          </CredenzaContent>
        </Credenza>
      ))}
    </div>
  );
}
