import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Reserve Your Seat | CNX Cigars Chiang Mai',
  description: 'Book your table at Chiang Mai’s premier cigar lounge. Select from our General Seating, VIP Lounge, or inquire about Private Events.',
};

export default function ReservationLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
