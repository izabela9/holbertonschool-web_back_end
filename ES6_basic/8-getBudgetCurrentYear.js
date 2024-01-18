export default function getBudgetForCurrentYear(income, gdp, capita) {
  const currentYear = new Date().getFullYear();
  return {
    income: income,
    gdp: gdp,
    capita: capita,
    year: currentYear,
  };
}
