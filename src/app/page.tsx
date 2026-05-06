import Navbar from '@/components/Navbar';
import Hero from '@/components/Hero';
import Awards from '@/components/Awards';
import FilterableMenu from '@/components/FilterableMenu';
import Footer from '@/components/Footer';
import Image from 'next/image';
import Link from 'next/link';
import styles from './page.module.css';

const BRANDS = [
  { name: 'Cohiba', desc: "Cuba's most iconic marque." },
  { name: 'Montecristo', desc: "The world's best-selling Cuban cigar." },
  { name: 'Romeo y Julieta', desc: 'Elegance and complexity in equal measure.' },
  { name: 'Partagas', desc: 'Bold, rich, and unapologetically full-bodied.' },
  { name: 'Bolivar', desc: 'Robust, earthy, and powerfully complex.' },
  { name: 'Davidoff', desc: 'Swiss precision meets Cuban tradition.' },
];

export default function Home() {
  return (
    <main className={styles.main}>
      <Navbar />
      <Hero />

      {/* ── THE EXPERIENCE ── */}
      <section id="experience" className={styles.experienceSection}>
        <div className={styles.splitLeft}>
          <div className={styles.imgBlock} style={{ position: 'relative', width: '100%', height: '100%' }}>
            <Image src="/lounge-chairs.jpg" alt="CNX Cigars Lounge Interior" fill style={{ objectFit: 'cover' }} />
          </div>
        </div>
        <div className={styles.splitRight}>
          <p className={styles.eyebrow}>The Experience</p>
          <h2 className={styles.sectionTitle}>Where Comfort<br />Becomes Culture</h2>
          <p className={styles.bodyText}>
            Sink into hand-crafted seating, order your pour, and let the evening
            unfold at its own pace. CNX Cigars is not a store — it is a destination.
          </p>
          <p className={styles.bodyText}>
            Our space is designed for those who appreciate the finer things: the
            weight of a perfectly rolled vitola, the haze of a great conversation,
            and the warmth of a room that knows how to slow time down.
          </p>
          <Link href="/reservation" className={styles.sectionCta}>Reserve Your Evening</Link>
        </div>
      </section>

      {/* ── OUR STORY ── */}
      <section id="story" className={styles.storySection}>
        <div className={styles.storyInner}>
          <p className={styles.eyebrow}>Our Story</p>
          <h2 className={styles.storySectionTitle}>Built on Passion.<br />Rooted in Craft.</h2>
          <div className={styles.storyColumns}>
            <div>
              <p className={styles.storyLead}>
                CNX Cigars was born from a journey that started in Havana in 1997 —
                a trip that changed everything.
              </p>
              <p className={styles.bodyText}>
                Walking the streets of the Vuelta Abajo, watching torcedores roll
                leaves with the quiet confidence of a lifetime's practice, our founders
                understood that a great cigar is not a product. It is a philosophy.
              </p>
              <p className={styles.bodyText}>
                Twenty-seven years later, that philosophy lives on in the heart of
                Chiang Mai's Nimman district. We brought Havana's spirit north — and
                Northern Thailand has never looked back.
              </p>
            </div>
            <div>
              <p className={styles.bodyText}>
                Today, CNX Cigars holds the <strong>largest selection of premium cigars
                in all of Northern Thailand</strong> — not because we count our inventory,
                but because we obsess over every leaf in it.
              </p>
              <p className={styles.bodyText}>
                Our lounge is a place where expats, travellers, and locals come
                together over a shared ritual. A place where rank and background
                dissolve in the blue smoke of a perfectly lit torpedo.
              </p>
              <p className={styles.bodyText}>
                This is the vision: a community, not a counter.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ── COMMUNITY ── */}
      <section className={styles.communitySection}>
        <div className={styles.splitRight}>
          <p className={styles.eyebrow}>Community & Culture</p>
          <h2 className={styles.sectionTitle}>More Than a Lounge.<br />A Circle.</h2>
          <p className={styles.bodyText}>
            The best conversations we have heard happened between strangers who became
            regulars. CNX Cigars draws a crowd that bridges industries, nationalities,
            and perspectives — united only by a shared appreciation for the craft.
          </p>
          <p className={styles.bodyText}>
            Whether you come alone or with a group, you will leave with a table that
            feels like yours.
          </p>
        </div>
        <div className={styles.splitLeft}>
          <div className={styles.imgBlock} style={{ position: 'relative', width: '100%', height: '100%' }}>
            <Image src="/cigar-shelves.jpg" alt="CNX Cigars Community Gathering" fill style={{ objectFit: 'cover' }} />
          </div>
        </div>
      </section>

      {/* ── BAR EXPERIENCE ── */}
      <section className={styles.barSection}>
        <div className={styles.barOverlay} />
        <div className={styles.barBg}>
          <Image src="/bar-interior.jpg" alt="CNX Cigars Bar" fill style={{ objectFit: 'cover' }} />
        </div>
        <div className={styles.barContent}>
          <p className={styles.eyebrowLight}>The Bar</p>
          <h2 className={styles.barTitle}>Every Cigar Deserves<br />a Perfect Pairing</h2>
          <p className={styles.barSubtitle}>
            Premium spirits, curated cocktails, and knowledgeable staff ready to
            guide you through a pairing you will not soon forget.
          </p>
          <Link href="/reservation" className={styles.ctaPrimaryLight}>Reserve a Table</Link>
        </div>
      </section>

      {/* ── FEATURED BRANDS ── */}
      <section className={styles.brandsSection}>
        <div className={styles.brandsInner}>
          <p className={styles.eyebrow}>Our House Brands</p>
          <h2 className={styles.sectionTitle}>Icons of the Industry</h2>
          <div className={styles.brandsGrid}>
            {BRANDS.map(b => (
              <div key={b.name} className={styles.brandCard}>
                <h3 className={styles.brandName}>{b.name}</h3>
                <p className={styles.brandDesc}>{b.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── MENU ── */}
      <FilterableMenu />
      <Awards />

      <Footer />
    </main>
  );
}
