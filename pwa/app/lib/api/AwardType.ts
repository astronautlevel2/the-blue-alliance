// https://raw.githubusercontent.com/the-blue-alliance/the-blue-alliance/master/consts/award_type.py
export enum AwardType {
  CHAIRMANS = 0,
  WINNER = 1,
  FINALIST = 2,
  WOODIE_FLOWERS = 3,
  DEANS_LIST = 4,
  VOLUNTEER = 5,
  FOUNDERS = 6,
  BART_KAMEN_MEMORIAL = 7,
  MAKE_IT_LOUD = 8,
  ENGINEERING_INSPIRATION = 9,
  ROOKIE_ALL_STAR = 10,
  GRACIOUS_PROFESSIONALISM = 11,
  COOPERTITION = 12,
  JUDGES = 13,
  HIGHEST_ROOKIE_SEED = 14,
  ROOKIE_INSPIRATION = 15,
  INDUSTRIAL_DESIGN = 16,
  QUALITY = 17,
  SAFETY = 18,
  SPORTSMANSHIP = 19,
  CREATIVITY = 20,
  ENGINEERING_EXCELLENCE = 21,
  ENTREPRENEURSHIP = 22,
  EXCELLENCE_IN_DESIGN = 23,
  EXCELLENCE_IN_DESIGN_CAD = 24,
  EXCELLENCE_IN_DESIGN_ANIMATION = 25,
  DRIVING_TOMORROWS_TECHNOLOGY = 26,
  IMAGERY = 27,
  MEDIA_AND_TECHNOLOGY = 28,
  INNOVATION_IN_CONTROL = 29,
  SPIRIT = 30,
  WEBSITE = 31,
  VISUALIZATION = 32,
  AUTODESK_INVENTOR = 33,
  FUTURE_INNOVATOR = 34,
  RECOGNITION_OF_EXTRAORDINARY_SERVICE = 35,
  OUTSTANDING_CART = 36,
  WSU_AIM_HIGHER = 37,
  LEADERSHIP_IN_CONTROL = 38,
  NUM_1_SEED = 39,
  INCREDIBLE_PLAY = 40,
  PEOPLES_CHOICE_ANIMATION = 41,
  VISUALIZATION_RISING_STAR = 42,
  BEST_OFFENSIVE_ROUND = 43,
  BEST_PLAY_OF_THE_DAY = 44,
  FEATHERWEIGHT_IN_THE_FINALS = 45,
  MOST_PHOTOGENIC = 46,
  OUTSTANDING_DEFENSE = 47,
  POWER_TO_SIMPLIFY = 48,
  AGAINST_ALL_ODDS = 49,
  RISING_STAR = 50,
  CHAIRMANS_HONORABLE_MENTION = 51,
  CONTENT_COMMUNICATION_HONORABLE_MENTION = 52,
  TECHNICAL_EXECUTION_HONORABLE_MENTION = 53,
  REALIZATION = 54,
  REALIZATION_HONORABLE_MENTION = 55,
  DESIGN_YOUR_FUTURE = 56,
  DESIGN_YOUR_FUTURE_HONORABLE_MENTION = 57,
  SPECIAL_RECOGNITION_CHARACTER_ANIMATION = 58,
  HIGH_SCORE = 59,
  TEACHER_PIONEER = 60,
  BEST_CRAFTSMANSHIP = 61,
  BEST_DEFENSIVE_MATCH = 62,
  PLAY_OF_THE_DAY = 63,
  PROGRAMMING = 64,
  PROFESSIONALISM = 65,
  GOLDEN_CORNDOG = 66,
  MOST_IMPROVED_TEAM = 67,
  WILDCARD = 68,
  CHAIRMANS_FINALIST = 69,
  OTHER = 70,
  AUTONOMOUS = 71,
  INNOVATION_CHALLENGE_SEMI_FINALIST = 72,
  ROOKIE_GAME_CHANGER = 73,
  SKILLS_COMPETITION_WINNER = 74,
  SKILLS_COMPETITION_FINALIST = 75,
  ROOKIE_DESIGN = 76,
  ENGINEERING_DESIGN = 77,
  DESIGNERS = 78,
  CONCEPT = 79,
  GAME_DESIGN_CHALLENGE_WINNER = 80,
  GAME_DESIGN_CHALLENGE_FINALIST = 81,
  SUSTAINABILITY = 82,
}

export const BLUE_BANNER_AWARDS = new Set([
  AwardType.CHAIRMANS,
  AwardType.CHAIRMANS_FINALIST,
  AwardType.WINNER,
  AwardType.WOODIE_FLOWERS,
  AwardType.SKILLS_COMPETITION_WINNER,
  AwardType.GAME_DESIGN_CHALLENGE_WINNER,
]);

export const INDIVIDUAL_AWARDS = new Set([
  AwardType.WOODIE_FLOWERS,
  AwardType.DEANS_LIST,
  AwardType.VOLUNTEER,
  AwardType.FOUNDERS,
  AwardType.BART_KAMEN_MEMORIAL,
  AwardType.MAKE_IT_LOUD,
]);

export const NON_JUDGED_NON_TEAM_AWARDS = new Set([
  AwardType.HIGHEST_ROOKIE_SEED,
  AwardType.WOODIE_FLOWERS,
  AwardType.DEANS_LIST,
  AwardType.VOLUNTEER,
  AwardType.WINNER,
  AwardType.FINALIST,
  AwardType.WILDCARD,
]);

export const MACHINE_AWARDS = new Set([
  AwardType.AUTONOMOUS,
  AwardType.CREATIVITY,
  AwardType.ENGINEERING_EXCELLENCE,
  AwardType.INDUSTRIAL_DESIGN,
  AwardType.INNOVATION_IN_CONTROL,
  AwardType.QUALITY,
]);

export const TEAM_ATTRIBUTE_AWARDS = new Set([
  AwardType.ENGINEERING_INSPIRATION,
  AwardType.GRACIOUS_PROFESSIONALISM,
  AwardType.IMAGERY,
  AwardType.JUDGES,
  AwardType.ROOKIE_ALL_STAR,
  AwardType.ROOKIE_INSPIRATION,
  AwardType.SPIRIT,
  AwardType.SUSTAINABILITY,
]);

export const SUBMITTED_AWARDS = new Set([
  AwardType.CHAIRMANS,
  AwardType.CHAIRMANS_FINALIST,
  AwardType.DEANS_LIST,
  AwardType.SAFETY,
  AwardType.WOODIE_FLOWERS,
]);

export const ROBOT_PERFORMANCE_AWARDS = new Set([
  AwardType.FINALIST,
  AwardType.WINNER,
]);

export enum AwardCategory {
  MACHINE_AWARDS = 1,
  TEAM_ATTRIBUTE_AWARDS = 2,
  SUBMITTED_AWARDS = 3,
  ROBOT_PERFORMANCE_AWARDS = 4,
}

export const SORT_ORDER: Partial<Record<AwardType, number>> = {
  [AwardType.CHAIRMANS]: 0,
  [AwardType.FOUNDERS]: 1,
  [AwardType.ENGINEERING_INSPIRATION]: 2,
  [AwardType.ROOKIE_ALL_STAR]: 3,
  [AwardType.WOODIE_FLOWERS]: 4,
  [AwardType.VOLUNTEER]: 5,
  [AwardType.DEANS_LIST]: 6,
  [AwardType.WINNER]: 7,
  [AwardType.FINALIST]: 8,
};
