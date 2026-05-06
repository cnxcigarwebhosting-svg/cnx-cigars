'use client';
import { useState } from 'react';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import styles from './reservation.module.css';

type SeatingType = 'General Seating' | 'VIP Lounge' | 'Private Event';

export default function ReservationPage() {
  const [seating, setSeating] = useState<SeatingType>('General Seating');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <>
      <Navbar />
      <main className={styles.page}>
        <div className={styles.hero}>
          <p className={styles.eyebrow}>Make a Reservation</p>
          <h1 className={styles.title}>Reserve Your Evening</h1>
          <p className={styles.subtitle}>
            Secure your place at Chiang Mai&apos;s most refined cigar lounge.
          </p>
        </div>

        <div className={styles.formWrap}>
          {submitted ? (
            <div className={styles.confirmation}>
              <div className={styles.confirmIcon}>✓</div>
              <h2>Reservation Received</h2>
              <p>
                Your reservation request has been received. Our team will contact
                you shortly to confirm your booking.
              </p>
            </div>
          ) : (
            <form className={styles.form} onSubmit={handleSubmit}>
              {/* Seating type */}
              <div className={styles.field}>
                <label className={styles.label}>Seating Preference</label>
                <div className={styles.seatingGrid}>
                  {(['General Seating', 'VIP Lounge', 'Private Event'] as SeatingType[]).map(opt => (
                    <button
                      type="button"
                      key={opt}
                      className={`${styles.seatingBtn} ${seating === opt ? styles.seatingActive : ''}`}
                      onClick={() => setSeating(opt)}
                    >
                      <span className={styles.seatingName}>{opt}</span>
                      <span className={styles.seatingHint}>
                        {opt === 'General Seating' && 'Walk-in or advance booking'}
                        {opt === 'VIP Lounge' && 'Dedicated section, priority service'}
                        {opt === 'Private Event' && 'Exclusive hire for your event'}
                      </span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Core fields */}
              <div className={styles.row}>
                <div className={styles.field}>
                  <label className={styles.label} htmlFor="name">Full Name</label>
                  <input id="name" type="text" className={styles.input} placeholder="Your name" required />
                </div>
                <div className={styles.field}>
                  <label className={styles.label} htmlFor="guests">Number of Guests</label>
                  <input id="guests" type="number" className={styles.input} placeholder="2" min={1} max={50} required />
                </div>
              </div>

              <div className={styles.row}>
                <div className={styles.field}>
                  <label className={styles.label} htmlFor="email">Email Address</label>
                  <input id="email" type="email" className={styles.input} placeholder="your@email.com" required />
                </div>
                <div className={styles.field}>
                  <label className={styles.label} htmlFor="phone">Phone / WhatsApp</label>
                  <input id="phone" type="tel" className={styles.input} placeholder="+66 6X XXX XXXX" />
                </div>
              </div>

              <div className={styles.row}>
                <div className={styles.field}>
                  <label className={styles.label} htmlFor="date">Date</label>
                  <input id="date" type="date" className={styles.input} required />
                </div>
                <div className={styles.field}>
                  <label className={styles.label} htmlFor="time">Preferred Time</label>
                  <input id="time" type="time" className={styles.input} required />
                </div>
              </div>

              {/* Private Event extra fields */}
              {seating === 'Private Event' && (
                <div className={`${styles.privateFields} animate-fade-in`}>
                  <div className={styles.field}>
                    <label className={styles.label} htmlFor="eventType">Event Type</label>
                    <select id="eventType" className={styles.input}>
                      <option value="">— Select type —</option>
                      <option>Corporate Event</option>
                      <option>Birthday Celebration</option>
                      <option>Client Entertainment</option>
                      <option>Social Gathering</option>
                      <option>Other</option>
                    </select>
                  </div>
                  <div className={styles.field}>
                    <label className={styles.label} htmlFor="specialRequests">Special Requests</label>
                    <textarea
                      id="specialRequests"
                      className={`${styles.input} ${styles.textarea}`}
                      placeholder="Tell us about your event — catering, décor, cigars selection, A/V needs…"
                      rows={4}
                    />
                  </div>
                </div>
              )}

              <div className={styles.field}>
                <label className={styles.label} htmlFor="notes">Additional Notes</label>
                <textarea
                  id="notes"
                  className={`${styles.input} ${styles.textarea}`}
                  placeholder="Any dietary requirements, accessibility needs, or preferences…"
                  rows={3}
                />
              </div>

              <button type="submit" className={styles.submitBtn}>
                Confirm Reservation Request
              </button>

              <p className={styles.disclaimer}>
                Our team will confirm your booking via email or WhatsApp within 24 hours.
              </p>
            </form>
          )}
        </div>
      </main>
      <Footer />
    </>
  );
}
