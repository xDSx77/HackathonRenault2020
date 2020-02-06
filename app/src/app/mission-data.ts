import { Coordinates } from './coordinates';

export interface MissionData {
  // Mission description
  mission: string;
  positions: Array<Coordinates>;
}
