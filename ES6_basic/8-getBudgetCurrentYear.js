export default function getBudgetForCurrentYear(income, gdp, capita) {
  const currentYear = new Date().getFullYear();
  return {
    income,
    gdp,
    capita,
    year: currentYear,
  };
}
