import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import styles from './contact.module.css';

export default function ContactPage() {
  return (
    <>
      <Navbar />
      <main className={styles.page}>
        <div className={styles.hero}>
          <p className={styles.eyebrow}>Get in Touch</p>
          <h1 className={styles.title}>Find Us at the Lounge</h1>
          <p className={styles.subtitle}>
            We are open every evening. Walk in, or reach out before you arrive.
          </p>
        </div>

        <div className={styles.body}>
          {/* Info cards */}
          <div className={styles.infoGrid}>
            <div className={styles.infoCard}>
              <h3 className={styles.cardTitle}>Location</h3>
              <p className={styles.cardText}>
                NPARC Building (2nd Floor)<br />
                45 Nimmanhaemin Soi 11<br />
                Tambon Su Thep, Mueang<br />
                Chiang Mai 50200, Thailand
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3 className={styles.cardTitle}>Opening Hours</h3>
              <table className={styles.hoursTable}>
                <tbody>
                  <tr><td>Monday – Thursday</td><td>5:00 PM – 1:00 AM</td></tr>
                  <tr><td>Friday – Saturday</td><td>5:00 PM – 2:00 AM</td></tr>
                  <tr><td>Sunday</td><td>4:00 PM – 12:00 AM</td></tr>
                </tbody>
              </table>
            </div>

            <div className={styles.infoCard}>
              <h3 className={styles.cardTitle}>Contact Us</h3>
              <ul className={styles.contactList}>
                <li>
                  <span className={styles.contactLabel}>WhatsApp</span>
                  <a href="https://wa.me/66622769937" className={styles.contactValue}>+66 62 276 9937</a>
                </li>
                <li>
                  <span className={styles.contactLabel}>LINE ID</span>
                  <span className={styles.contactValue}>Bodazey</span>
                </li>
                <li>
                  <span className={styles.contactLabel}>Email</span>
                  <a href="mailto:cigarschiangmai@gmail.com" className={styles.contactValue}>cigarschiangmai@gmail.com</a>
                </li>
              </ul>
            </div>
          </div>

          {/* Map */}
          <div className={styles.mapSection}>
            <h2 className={styles.mapTitle}>Find Us</h2>
            <div className={styles.mapWrapper}>
              <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3777.0605929653835!2d98.9649174154848!3d18.79796038724286!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30da3a00259e88cb%3A0xbce5c739a859e2ab!2sCNX%20Cigars%20International%20Cigar%20Bar%20and%20lounge!5e0!3m2!1sen!2sth!4v1714777200000!5m2!1sen!2sth"
                width="100%"
                height="100%"
                style={{ border: 0 }}
                allowFullScreen
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
              />
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}
