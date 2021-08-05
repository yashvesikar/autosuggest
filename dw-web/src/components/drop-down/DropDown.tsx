import styles from "./DropDown.module.scss";

interface IDropDownProps {
  isOpen: boolean;
  autoSuggestTerms: string[][]
}

export function DropDown(props: IDropDownProps) {
  const { isOpen, autoSuggestTerms: suggestions } = props;
  
  return (
    <div className={styles.dropDownContainer} style={isOpen ? {} : { display: "none" }}>
      <ul className={styles.listContainer}>
        {
          suggestions.map((suggestion) => {
            const [id, autoSuggestion] = suggestion;
            return <li key={id} className={styles.listItem}>{autoSuggestion}</li>;
          })
        }
      </ul>
    </div>
  )
}