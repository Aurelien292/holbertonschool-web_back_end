export default function cleanSet(set, startString) {
  if (startString === '') {
    return [...set].join('-');
  }

  const filtered = [...set]
    .filter((item) => item.startsWith(startString))
    .map((item) => item.slice(startString.length));

  return filtered.join('-');
}
