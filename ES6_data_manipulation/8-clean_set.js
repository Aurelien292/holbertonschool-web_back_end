export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  const filtered = [...set]
    .filter((item) => item.startsWith(startString))
    .map((item) => item.slice(startString.length));

  return filtered.join('-');
}
